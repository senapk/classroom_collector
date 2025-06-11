package main

import "fmt"

func main() {
	var a, b, c, t float32
	fmt.Scan(&a, &b, &c, &t)
	total := a + b + c
	menor := a
	if b < menor {
		menor = b
	}
	if c < menor {
		menor = c
	}
	total -= menor
	total += t
	total /= 3.0
	if total < 7 {
		fmt.Printf("Final com %.1f\n", total)
	} else {
		fmt.Printf("Aprovado com %.1f\n", total)
	}
}
