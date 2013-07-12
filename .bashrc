# .bashrc

# User specific aliases and functions

HOME=/home/usunoda

PATH=$PATH:${HOME}/scripts

function _asadmin() { sudo -u tcuser /TARe/apps/glassfish3/glassfish/bin/asadmin --user admin --passwordfile /TARe/apps/conf/glassfish_password.txt $@; }
export _asadmin

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
