# ARRAY — BASIC TRAVERSAL

## 1. What is an Array?

An array is a collection of elements stored in a sequence.

Example:

```python
arr = [10, 20, 30, 40, 50]
```

Here:

```text
10  20  30  40  50
↑   ↑   ↑   ↑   ↑
0   1   2   3   4    ← index
```

Each element has a position called an **index**.

In Python, indexing starts from `0`.

So:

```python
arr[0] = 10
arr[1] = 20
arr[2] = 30
arr[3] = 40
arr[4] = 50
```

### Important

```text
index → position
element → value stored at that position
```

For example:

```python
arr[2]
```

means:

> Give me the element present at index `2`.

Answer:

```text
30
```

---

# 2. What is Traversal?

**Traversal means visiting the elements of an array one by one.**

Example:

```python
arr = [10, 20, 30, 40]
```

Traversal means:

```text
10 → 20 → 30 → 40
```

We visit:

```text
arr[0]
arr[1]
arr[2]
arr[3]
```

Traversal is one of the most basic and most important operations in DSA.

Many array problems are simply:

```text
Traverse the array
        ↓
Look at each element
        ↓
Perform some operation
        ↓
Maintain/update some answer
```

---

# 3. Why Do We Need Traversal?

Suppose we want to find the largest number:

```text
[4, 8, 2, 9, 1]
```

We cannot know the largest element without checking the elements.

So we visit:

```text
4 → 8 → 2 → 9 → 1
```

and compare them.

Therefore, traversal is the basic foundation behind problems such as:

- Find maximum
- Find minimum
- Find second largest
- Count elements
- Search an element
- Check whether an array is sorted
- Count positive/negative/even/odd elements
- Find an element satisfying a condition

---

# 4. Traversal Using Index

The most common way to traverse an array in DSA is using an index.

```python
arr = [10, 20, 30, 40]

for i in range(len(arr)):
    print(arr[i])
```

Output:

```text
10
20
30
40
```

Let's understand this carefully.

### `len(arr)`

```python
len(arr)
```

gives the number of elements.

For:

```python
arr = [10, 20, 30, 40]
```

we get:

```text
len(arr) = 4
```

Therefore:

```python
range(len(arr))
```

becomes:

```python
range(4)
```

which produces:

```text
0
1
2
3
```

These are exactly the valid indexes.

Therefore:

```python
for i in range(len(arr)):
```

means:

```text
i = 0
i = 1
i = 2
i = 3
```

And:

```python
arr[i]
```

gives:

```text
arr[0] → 10
arr[1] → 20
arr[2] → 30
arr[3] → 40
```

---

# 5. `i` and `arr[i]`

This is VERY important.

Beginners often confuse these two.

Consider:

```python
arr = [5, 8, 2]
```

During traversal:

```python
for i in range(len(arr)):
```

### First iteration

```text
i = 0
arr[i] = arr[0] = 5
```

### Second iteration

```text
i = 1
arr[i] = arr[1] = 8
```

### Third iteration

```text
i = 2
arr[i] = arr[2] = 2
```

So:

```text
i       → index
arr[i]  → value
```

Remember this:

> **`i` tells us WHERE the element is. `arr[i]` tells us WHAT the element is.**

---

# 6. Forward Traversal

Forward traversal means moving from the first element to the last.

Example:

```python
arr = [10, 20, 30, 40]
```

We move:

```text
0 → 1 → 2 → 3
```

Code:

```python
for i in range(len(arr)):
    print(arr[i])
```

This is called **left-to-right traversal** or **forward traversal**.

---

# 7. Reverse Traversal

Sometimes we need to visit elements from the last element to the first.

Example:

```python
arr = [10, 20, 30, 40]
```

Reverse traversal:

```text
40 → 30 → 20 → 10
```

Indexes:

```text
3 → 2 → 1 → 0
```

Python:

```python
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])
```

Why?

```python
len(arr) - 1
```

gives the last index.

For an array of length `4`:

```text
len(arr) = 4
last index = 3
```

So:

```python
range(3, -1, -1)
```

produces:

```text
3
2
1
0
```

---

# 8. Traversal Without Index

Python also allows:

```python
arr = [10, 20, 30, 40]

for value in arr:
    print(value)
```

Here `value` directly contains the element.

```text
value = 10
value = 20
value = 30
value = 40
```

There is no need to use:

```python
arr[i]
```

### Then why do we learn index-based traversal?

Because DSA problems frequently require the **index**.

For example:

> Find the position of a target element.

Then we need:

```python
i
```

Therefore, understand both:

```python
for i in range(len(arr)):
```

and:

```python
for value in arr:
```

---

# 9. Traversal + Condition

Traversal becomes useful when we combine it with a condition.

Example:

> Count even numbers.

Array:

```text
[2, 5, 8, 3, 10]
```

We visit every element:

```text
2 → 5 → 8 → 3 → 10
```

For every element:

```text
Is it even?
```

If yes, increase the count.

Concept:

```text
count = 0

traverse
   ↓
check condition
   ↓
if condition is true
   ↓
count += 1
```

Code:

```python
count = 0

for value in arr:
    if value % 2 == 0:
        count += 1
```

This is an important general pattern:

> **Traverse → Check condition → Perform action**

---

# 10. Traversal + Searching

Suppose:

```python
arr = [4, 7, 2, 9, 5]
target = 9
```

We want to know whether `9` exists.

Traverse:

```text
4 → 7 → 2 → 9
```

At every element:

```text
current element == target?
```

When we find:

```text
9 == 9
```

we found it.

Basic idea:

```python
for i in range(len(arr)):
    if arr[i] == target:
        # found
```

This is called **linear search** because we may have to check elements one by one.

---

# 11. Traversal + Maintaining a Variable

This is one of the MOST IMPORTANT ideas in array problems.

Suppose:

```text
[4, 8, 2, 9, 1]
```

We want the maximum.

We create a variable:

```text
maximum
```

This variable stores the best answer we have found so far.

Start:

```text
maximum = 4
```

Then traverse:

```text
8 > 4
```

Update:

```text
maximum = 8
```

Then:

```text
2 > 8? No
```

Keep:

```text
maximum = 8
```

Then:

```text
9 > 8
```

Update:

```text
maximum = 9
```

Then:

```text
1 > 9? No
```

Final:

```text
maximum = 9
```

The general pattern is:

```text
Create answer variable
        ↓
Traverse array
        ↓
Compare current element with answer
        ↓
Update answer if required
```

This idea appears again and again in DSA.

---

# 12. What Does "Current" Mean?

During traversal, we often talk about the **current element**.

Example:

```python
for i in range(len(arr)):
```

The current element is:

```python
arr[i]
```

Suppose:

```text
i = 2
```

Then:

```text
current element = arr[2]
```

If:

```python
arr = [4, 8, 2, 9]
```

then:

```text
arr[2] = 2
```

So:

> **Current element means the element we are currently processing during traversal.**

---

# 13. Traversal + Counting

Another common pattern is counting.

Example:

> Count numbers greater than 5.

```text
[2, 8, 4, 10, 3, 7]
```

Create:

```text
count = 0
```

Traverse:

```text
2 → not greater than 5
8 → yes → count = 1
4 → no
10 → yes → count = 2
3 → no
7 → yes → count = 3
```

Answer:

```text
3
```

General pattern:

```text
count = 0

for every element:
    if condition:
        count += 1
```

---

# 14. Traversal + Boolean Variable

Sometimes we don't need a count. We only need to know whether something is true or false.

Example:

> Check whether every element is positive.

Array:

```text
[2, 5, 8, 1]
```

We can maintain:

```text
is_positive = True
```

During traversal, if we find:

```text
element <= 0
```

we know the condition has failed.

This gives another pattern:

```text
Assume condition is true
        ↓
Traverse
        ↓
If a violating element is found
        ↓
Change answer to False
```

This type of thinking is useful for:

- Check sorted array
- Check all positive
- Check all even
- Check whether a condition is satisfied

---

# 15. Traversal for Minimum

Finding minimum is the same idea as maximum.

Example:

```text
[7, 3, 9, 2, 8]
```

Start with:

```text
minimum = 7
```

Then:

```text
3 < 7 → minimum = 3
9 < 3 → no
2 < 3 → minimum = 2
8 < 2 → no
```

Answer:

```text
2
```

So maximum and minimum use the same general pattern:

```text
Traverse
   ↓
Compare
   ↓
Update answer
```

Only the comparison changes.

---

# 16. Initialization of the Answer Variable

This is a very important detail.

Suppose:

```text
arr = [-10, -5, -20]
```

If you write:

```python
maximum = 0
```

you have made a mistake.

Why?

There is no `0` in the array, and all numbers are negative.

The answer should be:

```text
-5
```

So a safer method is:

```python
maximum = arr[0]
```

Then start traversal from the next element.

Example:

```python
maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
```

This is an important interview habit:

> **Initialize your answer using a valid element or an appropriate extreme value.**

---

# 17. Why Start From Index 1?

If we already use:

```python
maximum = arr[0]
```

then index `0` has already been processed.

Therefore we don't need to compare it with itself again.

So:

```python
for i in range(1, len(arr)):
```

means:

```text
start from index 1
```

Example:

```text
arr = [5, 8, 2, 9]

maximum = arr[0] = 5

i = 1 → 8
i = 2 → 2
i = 3 → 9
```

This is very common in DSA.

---

# 18. Empty Array — Edge Case

Consider:

```python
arr = []
```

There is no:

```python
arr[0]
```

Therefore:

```python
maximum = arr[0]
```

would cause an error.

So before accessing `arr[0]`, we should know whether the array is empty.

General idea:

```text
If array is empty:
    handle empty case
Else:
    process array
```

You should always think about **edge cases**.

Important edge cases include:

- Empty array
- One element
- All elements equal
- All elements negative
- Already sorted
- Reverse sorted

---

# 19. Single Element Array

Example:

```text
[7]
```

Maximum is:

```text
7
```

Minimum is:

```text
7
```

There is no need for complicated logic.

This is why testing small examples is useful.

---

# 20. Time Complexity of Basic Traversal

Suppose the array contains `n` elements.

If we visit every element once:

```python
for i in range(len(arr)):
```

we perform approximately `n` operations.

Therefore:

```text
Time Complexity = O(n)
```

Why?

Because if the array doubles:

```text
n → 2n
```

the amount of work also roughly doubles.

---

# 21. Space Complexity of Basic Traversal

If we only use a few variables:

```python
maximum
count
i
```

we are not creating another array.

Therefore:

```text
Space Complexity = O(1)
```

This means the extra memory does not grow with `n`.

Important:

```text
O(n) time
O(1) extra space
```

is very common for basic array traversal.

---

# 22. Nested Traversal

Sometimes we use one loop inside another.

Example:

```python
for i in range(n):
    for j in range(n):
        print(arr[i], arr[j])
```

The outer loop runs `n` times.

The inner loop also runs `n` times for each outer iteration.

Therefore:

```text
n × n = n²
```

Time complexity:

```text
O(n²)
```

This is different from simple traversal:

```text
O(n)
```

### Important distinction

```text
One traversal       → O(n)

Traversal inside traversal → O(n²)
```

For basic array problems, always first ask:

> **Can I solve this with one traversal instead of nested loops?**

---

# 23. The General Basic Traversal Template

Most basic traversal problems can start from this mental template:

```text
1. Understand what the question asks.
2. Decide what information I need to maintain.
3. Traverse the array.
4. Process the current element.
5. Update the answer.
6. Return the answer.
```

In Python:

```python
answer = initial_value

for i in range(len(arr)):
    current = arr[i]

    # process current element

    # update answer

return answer
```

The exact `answer` and update condition will change from problem to problem.

---

# 24. Four Main Types of Basic Traversal Problems

When you see an array problem, first identify which type it is.

### Type 1 — FIND

Find something.

Examples:

```text
Largest element
Smallest element
Second largest
```

Typical thinking:

```text
maintain best answer
```

---

### Type 2 — COUNT

Count something.

Examples:

```text
Count even numbers
Count positive numbers
Count elements satisfying a condition
```

Typical thinking:

```text
count = 0
```

---

### Type 3 — CHECK

Check whether something is true.

Examples:

```text
Is array sorted?
Are all elements positive?
Does target exist?
```

Typical thinking:

```text
boolean / condition
```

---

### Type 4 — SEARCH

Find an element or its position.

Example:

```text
Find target = 7
```

Typical thinking:

```text
traverse
   ↓
compare current element with target
```

---

# 25. How to Recognize Basic Traversal

When you read a problem, look for words such as:

```text
find
maximum
minimum
largest
smallest
count
check
search
whether
each element
every element
```

These often suggest that you need to **traverse the array**.

But remember:

> The presence of these words does not automatically mean basic traversal is the optimal pattern.

For example, a problem may initially look like traversal but actually require:

```text
Hashing
Two Pointer
Sliding Window
Binary Search
Prefix Sum
```

So always consider the constraints and problem structure.

---

# 26. Most Important Mental Model

Do not memorize individual codes.

Understand this:

```text
ARRAY
  ↓
TRAVERSE
  ↓
CURRENT ELEMENT
  ↓
CHECK / COMPARE
  ↓
UPDATE SOMETHING
  ↓
ANSWER
```

For example:

### Maximum

```text
Traverse
→ compare
→ update maximum
```

### Count

```text
Traverse
→ check condition
→ increase count
```

### Search

```text
Traverse
→ compare with target
→ return position
```

### Check

```text
Traverse
→ check condition
→ detect violation
```

This is the real **Basic Traversal pattern**.

---

# 27. Common Beginner Mistakes

### Mistake 1 — Confusing index and value

Wrong thinking:

```text
i = element
```

Correct:

```text
i = index
arr[i] = element
```

---

### Mistake 2 — Wrong range

For:

```python
arr = [10, 20, 30]
```

valid indexes are:

```text
0, 1, 2
```

So:

```python
range(len(arr))
```

is correct.

---

### Mistake 3 — Using `arr[0]` on an empty array

Always consider:

```text
[]
```

---

### Mistake 4 — Initializing maximum to 0

This fails for:

```text
[-5, -2, -10]
```

Use an actual element or an appropriate extreme value.

---

### Mistake 5 — Using nested loops unnecessarily

Before writing:

```python
for i:
    for j:
```

ask:

> Can I solve this with one traversal?

---

# 28. What You Should Remember for Interviews

If the interviewer gives you a simple array problem, your first thought should be:

```text
Can I solve this by traversing the array once?
```

Then ask:

```text
What do I need to maintain?

maximum?
minimum?
count?
index?
boolean?
sum?
```

Then:

```text
Traverse → Process → Update → Return
```

This is the foundation on which many advanced array patterns are built.

---

# QUICK REVISION

## Basic Traversal

**Meaning:**

> Visiting every array element one by one and performing some operation.

### Main subtopics

```text
1. Array indexing
2. Forward traversal
3. Reverse traversal
4. Index vs value
5. Traversal using index
6. Traversal without index
7. Traversal + condition
8. Traversal + search
9. Traversal + counting
10. Traversal + min/max
11. Maintaining an answer
12. Boolean checking
13. Edge cases
14. Time complexity
15. Space complexity
16. Nested traversal
17. Pattern recognition
```

### Core template

```python
answer = initial_value

for i in range(len(arr)):
    current = arr[i]

    # process current

    # update answer
```

### Core idea

```text
Visit → Check/Compare → Update → Answer
```

### Typical complexity

```text
One traversal:
Time  → O(n)
Space → O(1)
```