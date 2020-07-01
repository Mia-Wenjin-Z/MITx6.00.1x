# Lec5_tuple_list

## Tuple

* `()`
* immutable, but can use `+`  to concact
* access by index
* `("one",)` notice the " `,` "
  * if ommited, `("one")` will be `"one"`
* use to swap value: `(x, y)` = `(y, x)`
* use to return multiple value in a function
* `range()` in essenece, is a tuple

## List

* `[]`

* can have mixed types (not encouraged)

* mutable with

  * `.append()` element (`add()` is used for set, not list)
  * `.extend(List2)` another list
  * `.pop()`  remove last
  * `.remove(val)`  remove the first `val`
  * `del(List[idx])` delete element at index `idx` 
  * `del List` -> break the reference
  * `List1 + List2` -> **return a copy!!!**
  * `sorted(List)` -> **return a copy!!**
  * `List.sort()` -> **sort list** (i.e., `Arrays.sort() or Collections.sort()` in java)

  A bit more about `del`: 

  ```python
   a=1       # 对象 1 被 变量a引用，对象1的引用计数器为1
   b=a       # 对象1 被变量b引用，对象1的引用计数器加1 = 2
   c=a       #1对象1 被变量c引用，对象1的引用计数器加1 = 3
   del a     #删除变量a，解除a对1的引用
   del b     #删除变量b，解除b对1的引用
   print(c)  #最终变量c仍然引用1 -> 1
  ```

### Clone, alias

* Clone list `list2 = list1[:]`
* **<u>No mutation during iteration</u>**

## String

* `list(s)` -> string to list
* `str(List)` -> list to string
* `s.split('<')` split by `<`
* `'<'.join(List) ` -> join elements by in list by `<`