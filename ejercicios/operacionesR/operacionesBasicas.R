#Un comentario se crea con #

#Para crear una variable podemos usar <- o = pero <- es el estandar y mas recomendable
#R diferencia entre mayusculas y minisculas
a <- 4
b <- 2

#Operaciones Basicas

#Suma
print(var1 + var2)

#Resta
print(var3 - var4)

#Division
print(var1 / var2)

#Multiplicacion
print(var3 * var4)

#Tipos de datos en R son texto, numeros, binarios y de logica(true or false)


#Vectores en R

vector1 <- c(1, 2, 3, 4, 5)

vector2 <- c("apple", "banana", "cherry")

#Estas tienen distintos metodos para modificar unir y accesar a los vectores

#Matrices en R

# crear vectores para las columnas de la matriz

warner <- c(20,20,16,15,14,6,12,16,24)
disney <- c(10,15,16,15,14,6,12,16,7)
fox <- c(15,14,17,15,12,16,15,9,14)

#creando matriz

peliculas <- matrix(c(warner,disney, fox),
                    nrow = 9,
                    ncol = 3)

print(peliculas)

#Este tiene distintos metodos para usar las matrices y explotar su potencial

#Listas en R

lista <- list(1, 2, 3)


#Esta tambien tiene distintos metodos 

#Factores en R

#Son estructuras de datos para manejar varibales categoricas (osea datos que toman una cantidad finita de valores Colores, Dia de semana, etc)

#Datos de Practica

#Queremos ver las ventas por talla (S/M/G)

#Ventas por talla

tallas <- c("m", "g", "s", "s", "m", "m")

#Crear factor

factorTallas <- factor(tallas,
                       levels = c("g", "m", "s"),
                       labels = c("G", "M", "S"))


#Grafica el factor

plot(factorTallas)



