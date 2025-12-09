# Go Lang

<https://go.dev>

> An open-source programming language supported by Google

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界")
}
```


## Learning Resources 

### Examples 

- [go by example](https://gobyexample.com/)

### Courses

- [free code camp Youtube](https://www.youtube.com/watch?v=YS4e4q9oBaU&t=288s)
- [udacity course](https://www.udacity.com/course/golang--cd11970) $250/month :yikes:
- [udemy go course](https://www.udemy.com/course/learn-go-the-complete-bootcamp-course-golang/learn/lecture/11665012?start=0#overview)
- [boot.dev go course](https://www.boot.dev/assignments/162d016b-c9b3-4a14-9be2-fd22c74c5710) and the [YouTube course](https://www.youtube.com/watch?v=un6ZyFkqFKo&t=712)
- [Effective Go](https://golang.org/doc/effective_go.html)*

## Community

- Gopher Slack
- [GoLang Bridge](https://golangbridge.org)

## Basics

- strong and static typed
- features:
  * simplicity
  * fast compile times
  * garbage collected
  * built-in concurrency

## Types

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
    // represents a Unicode code point

float32 float64

complex64 complex128
```

### Setting up a project

Set the `GOPATH` variable to your development folder

------

Before you begin work on a go module, you need to initialize it.
(if you aren't going to publish to `github`, you can use anything `foobar`, `me/stuff`, etc.)

```bash
go mod init github.com/dnorton/learn-go
```

install a library

This is going to put the binaries in your `GOPATH`

```bash
go get -u github.com/spf13/cobra/cobra
go: downloading github.com/spf13/cobra v1.8.0
go: module github.com/spf13/cobra@upgrade found (v1.8.0), but does not contain package github.com/spf13/cobra/cobra
```

To update all packages...

```bash
go get -u ./...
```

### Examples

- [hello server example](https://github.com/golang/example/blob/master/helloserver/server.go)

### Variables and Constants

```go
// Variable declaration
var name string = "John"
var age int = 30
var isActive bool = true

// Short declaration (inside functions only)
name := "John"
age := 30

// Multiple variables
var x, y int = 1, 2
a, b := "hello", "world"

// Constants
const Pi = 3.14
const (
    StatusOK = 200
    StatusNotFound = 404
)
```

### Control Flow

```go
// If statement
if x > 0 {
    fmt.Println("positive")
} else if x < 0 {
    fmt.Println("negative")
} else {
    fmt.Println("zero")
}

// If with initialization
if err := doSomething(); err != nil {
    return err
}

// Switch
switch day {
case "Monday":
    fmt.Println("Start of week")
case "Friday":
    fmt.Println("Almost weekend")
default:
    fmt.Println("Regular day")
}

// Switch without condition (cleaner than if-else chains)
switch {
case x > 0:
    fmt.Println("positive")
case x < 0:
    fmt.Println("negative")
default:
    fmt.Println("zero")
}
```

### Loops

```go
// Traditional for loop
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// While-style loop
for x < 100 {
    x += 10
}

// Infinite loop
for {
    // break to exit
}

// Range over slice/array
nums := []int{1, 2, 3, 4, 5}
for index, value := range nums {
    fmt.Printf("%d: %d\n", index, value)
}

// Range over map
m := map[string]int{"a": 1, "b": 2}
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}

// Ignore index/key with _
for _, value := range nums {
    fmt.Println(value)
}
```

### Functions

```go
// Basic function
func add(x int, y int) int {
    return x + y
}

// Multiple return values
func divide(x, y float64) (float64, error) {
    if y == 0 {
        return 0, errors.New("division by zero")
    }
    return x / y, nil
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return // naked return
}

// Variadic functions
func sum(nums ...int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}
```

### Arrays and Slices

```go
// Arrays (fixed size)
var arr [5]int
arr[0] = 1

// Array literal
primes := [5]int{2, 3, 5, 7, 11}

// Slices (dynamic size)
var s []int
s = append(s, 1, 2, 3)

// Slice literal
nums := []int{1, 2, 3, 4, 5}

// Make slice with capacity
s := make([]int, 5)      // len=5, cap=5
s := make([]int, 0, 5)   // len=0, cap=5

// Slicing
nums := []int{0, 1, 2, 3, 4, 5}
slice := nums[1:4]  // [1, 2, 3]
slice := nums[:3]   // [0, 1, 2]
slice := nums[3:]   // [3, 4, 5]
```

### Maps

```go
// Create map
ages := make(map[string]int)
ages["Alice"] = 30
ages["Bob"] = 25

// Map literal
ages := map[string]int{
    "Alice": 30,
    "Bob":   25,
}

// Check if key exists
age, exists := ages["Charlie"]
if exists {
    fmt.Println(age)
}

// Delete key
delete(ages, "Alice")
```

### Structs, Interfaces, and Methods

"A method is a function with a receiver."

```go
// Struct definition
type Person struct {
    Name string
    Age  int
}

// Create struct
p1 := Person{Name: "Alice", Age: 30}
p2 := Person{"Bob", 25}

// Method with value receiver
func (p Person) Greet() string {
    return "Hello, " + p.Name
}

// Method with pointer receiver (can modify)
func (p *Person) HaveBirthday() {
    p.Age++
}

// Interface definition
type Shape interface {
    Area() float64
    Perimeter() float64
}

// Implement interface
type Rectangle struct {
    Width, Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.Width + r.Height)
}
```

### Pointers

```go
// Create pointer
x := 5
p := &x  // p points to x

// Dereference pointer
*p = 10  // changes x to 10

// Pointers in functions
func increment(x *int) {
    *x++
}

n := 5
increment(&n)  // n is now 6
```

### Error Handling

```go
// Return error
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / b, nil
}

// Check error
result, err := divide(10, 0)
if err != nil {
    log.Fatal(err)
}

// Custom error type
type MyError struct {
    Code    int
    Message string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("error %d: %s", e.Code, e.Message)
}
```

### Goroutines and Channels

```go
// Start goroutine
go func() {
    fmt.Println("Running in goroutine")
}()

// Channels
ch := make(chan int)

// Send to channel
go func() {
    ch <- 42
}()

// Receive from channel
value := <-ch

// Buffered channel
ch := make(chan int, 10)

// Close channel
close(ch)

// Range over channel
for value := range ch {
    fmt.Println(value)
}

// Select statement (multiplexing)
select {
case msg1 := <-ch1:
    fmt.Println("Received", msg1)
case msg2 := <-ch2:
    fmt.Println("Received", msg2)
case <-time.After(time.Second):
    fmt.Println("Timeout")
}
```

### Defer, Panic, Recover

```go
// Defer (runs after function returns)
func example() {
    defer fmt.Println("World")
    fmt.Println("Hello")
}
// Prints: Hello\nWorld

// Multiple defers (LIFO order)
defer fmt.Println("1")
defer fmt.Println("2")
defer fmt.Println("3")
// Prints: 3\n2\n1

// Common use: cleanup
file, err := os.Open("file.txt")
if err != nil {
    return err
}
defer file.Close()

// Panic and recover
func mayPanic() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from:", r)
        }
    }()
    panic("something went wrong")
}
```

## Common Packages

### Standard Library

- [fmt](https://pkg.go.dev/fmt) - formatted I/O
- [os](https://pkg.go.dev/os) - operating system functions
- [io](https://pkg.go.dev/io) - I/O primitives
- [net/http](https://pkg.go.dev/net/http) - HTTP client and server
- [encoding/json](https://pkg.go.dev/encoding/json) - JSON encoding/decoding
- [time](https://pkg.go.dev/time) - time operations
- [strings](https://pkg.go.dev/strings) - string manipulation
- [strconv](https://pkg.go.dev/strconv) - string conversions
- [errors](https://pkg.go.dev/errors) - error handling
- [context](https://pkg.go.dev/context) - cancellation and deadlines
- [sync](https://pkg.go.dev/sync) - synchronization primitives
- [testing](https://pkg.go.dev/testing) - testing framework

### Popular Third-Party Libraries

- [gorilla/mux](https://github.com/gorilla/mux) - HTTP router
- [gin](https://github.com/gin-gonic/gin) - web framework
- [echo](https://github.com/labstack/echo) - web framework
- [cobra](https://github.com/spf13/cobra) - CLI applications
- [viper](https://github.com/spf13/viper) - configuration management
- [gorm](https://github.com/go-gorm/gorm) - ORM
- [sqlx](https://github.com/jmoiron/sqlx) - SQL extensions
- [logrus](https://github.com/sirupsen/logrus) - structured logging
- [zap](https://github.com/uber-go/zap) - fast logging
- [testify](https://github.com/stretchr/testify) - testing toolkit

## Common Patterns

### JSON Handling

```go
// Struct tags for JSON
type User struct {
    ID        int    `json:"id"`
    Name      string `json:"name"`
    Email     string `json:"email,omitempty"`
    Password  string `json:"-"` // never include in JSON
}

// Marshal (struct to JSON)
user := User{ID: 1, Name: "Alice"}
jsonData, err := json.Marshal(user)

// Unmarshal (JSON to struct)
var user User
err := json.Unmarshal(jsonData, &user)
```

### HTTP Server

```go
package main

import (
    "encoding/json"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]string{
        "message": "Hello, World!",
    })
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
```

### File I/O

```go
// Read entire file
data, err := os.ReadFile("file.txt")

// Write file
err := os.WriteFile("file.txt", []byte("content"), 0644)

// Open and read
file, err := os.Open("file.txt")
defer file.Close()
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
```

## Testing

```go
// Basic test (file: myfile_test.go)
package mypackage

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    if result != 5 {
        t.Errorf("Expected 5, got %d", result)
    }
}

// Table-driven tests
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive numbers", 2, 3, 5},
        {"negative numbers", -2, -3, -5},
        {"zero", 0, 0, 0},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("got %d, want %d", result, tt.expected)
            }
        })
    }
}
```

Run tests:
```bash
go test
go test -v          # verbose
go test ./...       # all packages
go test -cover      # with coverage
go test -bench=.    # run benchmarks
```

## Useful Commands

```bash
go run main.go              # Run program
go build                    # Compile current package
go build -o myapp          # Compile with custom name
go install                  # Install binary to $GOPATH/bin
go test                     # Run tests
go test -v                  # Verbose test output
go fmt                      # Format code
go vet                      # Examine code for mistakes
go mod tidy                 # Clean up dependencies
go mod vendor               # Copy dependencies to vendor/
go get package              # Add dependency
go list -m all              # List all dependencies
go doc fmt.Println          # Show documentation
```

## Tips and Best Practices

* Use `gofmt` or `goimports` to format code automatically
* Start goroutine names with lowercase (unexported)
* Use `make` for slices, maps, and channels
* Always handle errors - don't ignore them
* Use `context.Context` for cancellation and timeouts
* Prefer composition over inheritance
* Keep interfaces small (often just 1-2 methods)
* Use `go vet` and `golint` for code quality
* Name receivers consistently (usually first letter of type)
* Use table-driven tests
* Put binary data in `internal/` to prevent imports

