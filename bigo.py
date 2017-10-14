class Fibonacci:
    __fibocache = []
    def fibonaccirecur(self, numero): 
        if numero < 0:
            return " No se admiten valores menores a cero"
        elif numero < 2:
            return numero 
        return(self.fibonaccirecur(numero-1) + self.fibonaccirecur(numero-2))
    
    def fibonaccifor(self, numero):
        if numero < 0:
            return " No se admiten valores menores a cero"
        elif numero <= 2:
            return " "+str(1)
        fibo = 0
        previo = 1
        penultimo = 0
        cadena = "Cadena Fibonacci:"
        for x in range(numero):
            penultimo = fibo
            fibo = previo + penultimo
            cadena += " "+str(fibo)
            previo = penultimo
        return cadena

    def fibonacciarreglo(self, numero):        
        cache = {0:0,1:1}
        def fib(n):
            if n in cache:
                return cache[n]
            cache[n] = fib(n-1) + fib(n-2)
            return cache[n]
        return fib(numero)
            

            
