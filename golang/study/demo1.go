package main

import "fmt"

func main() {
	var as int = 12313
	var ds int = 16656
	var ax int
	ax = x(as, ds)
	fmt.Print(ax)
}

func x(a, b int) int {
	var result int
	if a < b {
		result = a
	} else {
		result = b
	}
	return result

}
