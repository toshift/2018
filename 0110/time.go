package main

import (
	"fmt"
	"os/exec"
	"runtime"
	"time"
)

func main() {
	fmt.Println("test")
	fmt.Println(time.Now())
	startBrowser("http://google.com")
}

func startBrowser(url string) bool {
	var args []string
	switch runtime.GOOS {
	case "windows":
		args = []string{"cmd", "/c", "start"}
	default:
		args = []string{"xdg-open"}
	}
	cmd := exec.Command(args[0], append(args[1:], url)...)
	return cmd.Start() == nil
}
