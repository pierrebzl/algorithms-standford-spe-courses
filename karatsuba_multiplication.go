package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func kara(x string, y string) uint64 {
	fmt.Println(x, y)

	// Base case
	if len(x) == 1 && len(y) == 1 {
		xi, _ := strconv.Atoi(x)
		yi, _ := strconv.Atoi(y)
		return uint64(xi) * uint64(yi)
	}

	// Leading 0 to make numbers the same length
	if len(x) < len(y) {
		for i := 0; i < len(y)-len(x)+1; i++ {
			x = "0" + x
		}
	}
	if len(y) < len(x) {
		for i := 0; i < len(x)-len(y)+1; i++ {
			y = "0" + y
		}
	}

	if len(x)%2 == 1 {
		x = "0" + x
	}
	if len(y)%2 == 1 {
		y = "0" + y
	}

	middle := (len(x) / 2)

	// Split
	x_l := x[:middle]
	xi_l, _ := strconv.ParseInt(x_l, 10, 64)
	x_r := x[middle:len(x)]
	xi_r, _ := strconv.ParseInt(x_r, 10, 64)
	y_l := y[:middle]
	yi_l, _ := strconv.ParseInt(y_l, 10, 64)
	y_r := y[middle:len(y)]
	yi_r, _ := strconv.ParseInt(y_r, 10, 64)

	fmt.Println("x", x_l, x_r)
	fmt.Println("y", y_l, y_r)

	// Recusive
	a := kara(x_l, y_l)
	b := kara(x_r, y_r)
	c := kara(strconv.FormatInt((xi_l+xi_r), 10), strconv.FormatInt((yi_l+yi_r), 10)) - a - b

	p := math.Pow10(2 * middle)
	q := math.Pow10(middle)

	return uint64(p)*uint64(a) + uint64(q)*uint64(c) + uint64(b)
}

func main() {
	x := os.Args[1]
	y := os.Args[2]

	res := kara(x, y)
	fmt.Println(res)
}
