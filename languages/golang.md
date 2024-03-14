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

```
 go get -u github.com/spf13/cobra/cobra
go: downloading github.com/spf13/cobra v1.8.0
go: module github.com/spf13/cobra@upgrade found (v1.8.0), but does not contain package github.com/spf13/cobra/cobra
```

### Examples

- [ ](https://github.com/golang/example/blob/master/helloserver/server.go)
