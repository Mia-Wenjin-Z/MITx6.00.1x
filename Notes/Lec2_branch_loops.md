# Lec2 branch_loops

## I/O

* input(""..."")
  * **input type is interpreted as a STRING!!**

![image-20200622183614320](/Users/miawenjinzhang/Library/Application Support/typora-user-images/image-20200622183614320.png)

![image-20200622183825650](/Users/miawenjinzhang/Library/Application Support/typora-user-images/image-20200622183825650.png)

* print

## Control flow

```python
	BRANCHING
1. if 

if [con1] else :
if [con1] elif [con2] else:

  LOOPING
2. while
while [con] :
	do something

3. for
for x in range (n): 
	do something ... x - [0, n)

                        
range(start, stop ,step) [start, end) += step
eg.
range(5, 11, 2)  -> 5, 7, 9  
                          
4. break : immediately jump out of the current loop
5. continue
```

## Guess and check

* Example - found square root
* Core: guess a value,check if correct -> exhaustive emuneration