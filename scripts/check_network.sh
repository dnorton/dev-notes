#!/bin/bash
# Network Diagnostic Script
# Helps diagnose whether network issues are router, wifi, or ISP related

echo "======================================"
echo "    Network Diagnostics Tool"
echo "======================================"
echo ""

# Get the gateway (router) IP
echo "=== Router Gateway Check ==="
GATEWAY=$(netstat -rn | grep default | grep en0 | awk '{print $2}' | head -1)
if [ -z "$GATEWAY" ]; then
    echo "ERROR: No gateway found. You may not be connected to wifi."
    exit 1
fi
echo "Gateway: $GATEWAY"
echo ""
echo "Pinging router (5 packets)..."
ping -c 5 "$GATEWAY"
PING_RESULT=$?

if [ $PING_RESULT -eq 0 ]; then
    echo "✓ Router is reachable"
else
    echo "✗ Cannot reach router - Router may be down or wifi disconnected"
fi

echo ""
echo "=== WiFi Signal Strength ==="
AIRPORT="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
if [ -f "$AIRPORT" ]; then
    $AIRPORT -I | grep -E "^ *(SSID|agrCtlRSSI|agrCtlNoise|channel|lastTxRate|maxRate)"

    # Extract RSSI and provide interpretation
    RSSI=$($AIRPORT -I | grep agrCtlRSSI | awk '{print $2}')
    if [ ! -z "$RSSI" ]; then
        echo ""
        if [ "$RSSI" -gt -50 ]; then
            echo "Signal: Excellent (RSSI: $RSSI)"
        elif [ "$RSSI" -gt -60 ]; then
            echo "Signal: Good (RSSI: $RSSI)"
        elif [ "$RSSI" -gt -70 ]; then
            echo "Signal: Fair (RSSI: $RSSI)"
        else
            echo "Signal: Poor (RSSI: $RSSI) - Consider moving closer to router"
        fi
    fi
else
    echo "Airport utility not found"
fi

echo ""
echo "=== DNS Resolution Check ==="
echo "Testing DNS lookup for google.com..."
DNS_START=$(date +%s%N)
nslookup google.com > /dev/null 2>&1
DNS_RESULT=$?
DNS_END=$(date +%s%N)
DNS_TIME=$(( (DNS_END - DNS_START) / 1000000 ))

if [ $DNS_RESULT -eq 0 ]; then
    echo "✓ DNS resolution working (${DNS_TIME}ms)"
    if [ $DNS_TIME -gt 500 ]; then
        echo "  Warning: DNS is slow (>${DNS_TIME}ms)"
    fi
else
    echo "✗ DNS resolution failed - Check router DNS settings"
fi

echo ""
echo "=== Internet Connectivity Check ==="
echo "Pinging 8.8.8.8 (Google DNS)..."
ping -c 3 8.8.8.8 > /dev/null 2>&1
INTERNET_RESULT=$?

if [ $INTERNET_RESULT -eq 0 ]; then
    echo "✓ Internet is reachable"
else
    echo "✗ Cannot reach internet - ISP or modem issue"
fi

echo ""
echo "=== Speed Test ==="
echo "Running networkQuality (this may take 10-20 seconds)..."
networkQuality

echo ""
echo "======================================"
echo "         Diagnostic Summary"
echo "======================================"
echo ""

# Provide diagnosis
if [ $PING_RESULT -ne 0 ]; then
    echo "DIAGNOSIS: Router problem or wifi disconnected"
    echo "ACTION: Restart your router/access point, or reconnect to wifi"
elif [ $INTERNET_RESULT -ne 0 ]; then
    echo "DIAGNOSIS: ISP or modem problem"
    echo "ACTION: Check modem, restart it, or contact ISP"
elif [ ! -z "$RSSI" ] && [ "$RSSI" -lt -70 ]; then
    echo "DIAGNOSIS: Weak wifi signal"
    echo "ACTION: Move closer to router or check for interference"
else
    echo "DIAGNOSIS: Network connectivity appears normal"
    echo "Check the speed test results above for performance issues"
fi

echo ""
