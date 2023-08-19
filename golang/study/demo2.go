package main

import "fmt"

func main() {
	var rei int
	rei = ds(11)
	fmt.Print(rei)
}

func ds(a int) int {
	var rei int
	if a <= 12 {
		rei = a - 4
		return rei
	} else {
		rei = 123
		return rei
	}

}
