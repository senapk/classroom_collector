package main

import "fmt"

func main() {
	var a, b, c, trab float64
	var menor, media float64

	fmt.Scanf("%f\n%f\n%f\n%f", &a, &b, &c, &trab)

	menor = a
	if b < menor {
		menor = b
	}
	if c < menor {
		menor = c
	}

	media = (a + b + c + trab - menor) / 3

	if media >= 7 {
		fmt.Printf("Aprovado com %.1f\n", media)
	} else {
		fmt.Printf("Final com %.1f\n", media)
	}
}
