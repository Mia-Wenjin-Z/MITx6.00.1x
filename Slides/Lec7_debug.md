# Lec7_debug

## Test

* Unit test: function test
* Regression test: test again the same unit to catch reintroduced errors
  * 纠正错误、添加新功能时，原有的test要能过
* Integration test: overall system (don't rush to do so)

### how to 

* Black box
  * Based on spec
* Glass box
  * **path complete** if all paths of the code is tested once -> hard to do with recursion
  * **path complete != correct code**
  * branches
  * for / while loops -> not enter/ enter once/ enter multiple times

## Bug

* Overt and persistent
  * Use defensive programming to make errors fall into this one
* Overt and intermittent
* Covert - worst

## Debugging

* print

  * enter
  * param
  * results
  * 二分法

* error messages

* logic

* Debugging Example: isPalindrome

  