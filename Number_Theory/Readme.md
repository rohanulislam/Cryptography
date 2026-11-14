# S. M. Rohanul Islam
## Student ID: IT23034 | Department of ICT, MBSTU

---
# Number Theory and Cryptography Workshop
**Maths and Physics Club, IIT Bombay**

This repository contains comprehensive study notes, mathematical proofs, algorithms, and complete solutions to the programming and theoretical assignments from the **Number Theory and Cryptography Workshop**.

---

## Table of Contents
* **Day 0: Foundations of Number Theory & Modular Arithmetic**
  * [0.1 Division with Remainder & Divisibility by 3](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=btjlPY8Nedy_&line=1&uniqifier=1)
  * [0.2 Modular Addition & Multiplication Tables](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=4YfgtamLtrxm&line=2&uniqifier=1)
* **Day 1: Core Number-Theoretic Algorithms**
  * [1.1 Naive GCD vs. Euclid's Algorithm](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=CX7X5RX_tw7w&line=2&uniqifier=1)
  * [1.2 Extended Euclid's Algorithm](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=66CfjFNet58F&line=1&uniqifier=1)
  * [1.3 Least Common Multiple (Naive vs. Fast LCM)](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=K7uziNd-t-N7&line=2&uniqifier=1)
  * [1.4 Fast Modular Exponentiation](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=mPw-0Yu4uFsc&line=2&uniqifier=1)
  * [1.5 Euler's Totient Function](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=AvNquistuJdD&line=2&uniqifier=1)
* **Day 2: Prime Numbers, Primality Testing & Conjectures**
  * [2.1 Sieve of Eratosthenes & Wheel Factorization (Mod 30)](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=I1m60_2QuPfT&line=2&uniqifier=1)
  * [2.2 Fermat Primality Test & Carmichael Numbers](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=vgdbfUpquVzt&line=2&uniqifier=1)
  * [2.3 Lucas-Lehmer Primality Test (Mersenne Primes)](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=ARu_rY-dub7d&line=2&uniqifier=1)
  * [2.4 Antiprimes (Highly Composite Numbers)](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=P8nldfClueM_&line=2&uniqifier=1)
* **Day 1 Assignment: Algorithmic Implementations**
  * [A1.1 Problem 1: Extended Euclid's Algorithm](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=AGL89HnavtGX&line=4&uniqifier=1)
  * [A1.2 Problem 2: Least Common Multiple](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=lXh_BhvCvv8W&line=2&uniqifier=1)
  * [A1.3 Problem 3: Linear Diophantine Equations](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=hmVV3lxCv16K&line=2&uniqifier=1)
  * [A1.4 Problem 4: Modular Multiplicative Inverse & Division](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=ZkoracjKv6WD&line=2&uniqifier=1)
  * [A1.5 Problem 5: Fast Modular Exponentiation](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=UYCeORjFv9ra&line=2&uniqifier=1)
  * [A1.6 Problem 6: Chinese Remainder Theorem](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=9xwbHXX7wC0c&line=2&uniqifier=1)
* **Day 2 Assignment: Theoretical & Computational Verification**
  * [A2.1 Problem 1: Repunits & Set A_p](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=pnUFDA2-wFj1&line=2&uniqifier=1)
  * [A2.2 Problem 2: Even Perfect Numbers (Euclid-Euler)](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=aBKXzhM-wJ8A&line=2&uniqifier=1)
  * [A2.3 Problem 3: Generating Fermat Pseudoprimes Base a](https://colab.research.google.com/drive/19MBD93JV4i1dj970PRBe-xL7g3mZWgD0#scrollTo=xZ93bZB3wMo-&line=2&uniqifier=1)

---

## Day 0: Foundations of Number Theory & Modular Arithmetic

### 1.1 Evolution of Number Systems
* **Natural Numbers ($\mathbb{N}$):** Originated from counting ($1, 2, 3, \dots$). Closed under addition and multiplication, but **not** closed under subtraction (e.g., $2 - 3 \notin \mathbb{N}$).
* **Integers ($\mathbb{Z}$):** Introduces $0$ and negative numbers ($\dots, -2, -1, 0, 1, 2, \dots$) to make subtraction always possible. Closed under $+, -, \times$, but **not** closed under division (e.g., $3/2 \notin \mathbb{Z}$).
* **Rational Numbers ($\mathbb{Q}$):** Introduces fractions to enable division. However, computer science and cryptography frequently require strictly **integer** solutions.
* **Significance:** Once thought to be purely abstract ("useless" according to G.H. Hardy), number theory is now the backbone of modern cryptography, high-speed computer arithmetic, and internet security.

### 1.2 Divisibility & Division with Remainder
* **Definition (Divisibility):** An integer $a$ is divisible by an integer $b$ (denoted $b \mid a$) if there exists an integer $k$ such that:
  $$a = b \times k$$
* **Key Properties:**
  1. If $c \mid a$ and $c \mid b$, then $c \mid (a \pm b)$.
  2. If $b \mid a$, then $b \mid (a \times c)$ for any integer $c$.
* **Division Algorithm:** For any integer $a$ and positive integer $b$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that:
  $$a = q \times b + r \quad \text{where } 0 \le r < b$$
  * *Example (Negative Dividend):* For $a = -13, b = 3$, we write $-13 = (-5) \times 3 + 2$, giving $q = -5$ and $r = 2$ (since $0 \le r < 3$).
* **Remainder Equivalence Lemma:** Integers $a_1$ and $a_2$ leave the same remainder upon division by $b$ if and only if $b \mid (a_1 - a_2)$.

### 1.3 Modular Arithmetic & Congruence Relations
* **Definition:** Two integers $a$ and $b$ are congruent modulo $m$ if they leave the same remainder when divided by $m$ (equivalently, $m \mid (a - b)$):
  $$a \equiv b \pmod m$$
* **Arithmetic Preservation:** If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then:
  * **Addition:** $a + c \equiv b + d \pmod m$
  * **Multiplication:** $a \times c \equiv b \times d \pmod m$
* **Application — Finding Last Digits:** To find the last two digits of $99^{99}$, compute $99^{99} \pmod{100}$:
  $$99 \equiv -1 \pmod{100} \implies 99^{99} \equiv (-1)^{99} \equiv -1 \equiv 99 \pmod{100}$$
* **Application — Divisibility by 3:** Since $10 \equiv 1 \pmod 3$, we have $10^k \equiv 1^k \equiv 1 \pmod 3$. Thus, any base-10 number $\sum d_k 10^k \equiv \sum d_k \pmod 3$.

### 1.4 Modular Operations & Cayley Tables
* **Modular Subtraction:** Always well-defined for any modulus $m$. Solving $a + x \equiv b \pmod m$ yields $x \equiv b - a \pmod m$.
* **Modular Division:** Solving $a \times x \equiv b \pmod m$ is **not** always possible for composite moduli!

```text
Multiplication Modulo 7 (Prime)          Multiplication Modulo 6 (Composite)
× | 0 1 2 3 4 5 6                        × | 0 1 2 3 4 5
--+--------------                        --+------------
0 | 0 0 0 0 0 0 0                        0 | 0 0 0 0 0 0
1 | 0 1 2 3 4 5 6                        1 | 0 1 2 3 4 5
2 | 0 2 4 6 1 3 5  <-- All remainders    2 | 0 2 4 0 2 4  <-- Missing 1, 3, 5
3 | 0 3 6 2 5 1 4      present in every  3 | 0 3 0 3 0 3  <-- 3x ≡ 1 (mod 6) has
4 | 0 4 1 5 2 6 3      non-zero row!     4 | 0 4 2 0 4 2      NO solution!
5 | 0 5 3 1 6 4 2                        5 | 0 5 4 3 2 1
6 | 0 6 5 4 3 2 1
```

---

## Day 1: Algorithmic Number Theory & Cryptographic Primitives

### 2.1 Greatest Common Divisor (GCD) & Euclid's Algorithm
* **Definition:** $\gcd(a, b)$ is the largest positive integer dividing both $a$ and $b$ (not both zero). By convention, $\gcd(a, 0) = a$.
* **Naive Approach:** Checking all integers from $\min(a,b)$ down to $1$ takes $O(\min(a, b))$ time—infeasible for 100-digit cryptographic keys.
* **Euclid's Lemma (Subtraction Form):** $d \mid a$ and $d \mid b \iff d \mid (a - b)$ and $d \mid b$.
* **Euclid's Algorithm (Modulo Form):** For $a \ge b > 0$:
  $$\gcd(a, b) = \gcd(b, a \bmod b)$$
* **Complexity Analysis:**
  * **Lemma:** If $a \ge b > 0$, then $(a \bmod b) < \frac{a}{2}$.
    * *Case 1 ($b \le a/2$):* $a \bmod b < b \le a/2$.
    * *Case 2 ($b > a/2$):* $a \bmod b = a - b < a/2$.
  * Because the larger argument drops by at least a factor of $2$ in every step, the algorithm runs in $O(\log_2 a + \log_2 b)$ iterations. Even for a 5,000-digit number ($a < 10^{5000}$), it takes fewer than $16,610$ iterations.

### 2.2 Extended Euclid's Algorithm
* **Bézout's Identity / Certificate:** $\gcd(a, b) = d$ can always be expressed as a linear combination:
  $$ax + by = d \quad \text{for some } x, y \in \mathbb{Z}$$
* **Recursive Derivation:** Suppose $d = \gcd(b, a \bmod b) = bp + (a \bmod b)q$. Using the identity $a \bmod b = a - \lfloor \frac{a}{b} \rfloor b$:
  $$d = bp + \left(a - \left\lfloor \frac{a}{b} \right\rfloor b\right)q = aq + b\left(p - \left\lfloor \frac{a}{b} \right\rfloor q\right)$$
  Thus, $x = q$ and $y = p - \lfloor \frac{a}{b} \rfloor q$.

### 2.3 Least Common Multiple (LCM)
* **Definition:** $\text{lcm}(a, b)$ is the smallest positive integer divisible by both $a$ and $b$.
* **Fundamental Identity:**
  $$\text{lcm}(a, b) \cdot \gcd(a, b) = a \cdot b \implies \text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$$

### 2.4 Linear Diophantine Equations
* **Existence Theorem:** The equation $ax + by = c$ (with $a, b$ not both zero) has integer solutions $(x, y)$ **if and only if** $d = \gcd(a, b)$ divides $c$ ($d \mid c$).
* **Finding a Particular Solution:**
  1. Run Extended Euclid's Algorithm to find $(\bar{x}, \bar{y})$ such that $a\bar{x} + b\bar{y} = d$.
  2. Multiply by $t = c / d$: $(x_0, y_0) = (t\bar{x}, t\bar{y})$.
* **General Solution (All Solutions):** Let $a = dp$ and $b = dq$ (so $\gcd(p, q) = 1$). Given one solution $(x_0, y_0)$, all integer solutions are parameterized by $t \in \mathbb{Z}$:
  $$x = x_0 + tq, \qquad y = y_0 - tp$$

### 2.5 Modular Division & Multiplicative Inverses
* **Multiplicative Inverse:** An integer $\bar{a}$ is the inverse of $a \pmod n$ if $a \cdot \bar{a} \equiv 1 \pmod n$.
* **Existence & Uniqueness:**
  * The inverse exists **if and only if** $\gcd(a, n) = 1$.
  * When it exists, it is unique modulo $n$.
* **Computing $b / a \pmod n$:**
  1. Solve $ax + ny = 1$ using Extended Euclid's Algorithm.
  2. Then $\bar{a} = x \bmod n$.
  3. Compute $b / a \equiv b \cdot \bar{a} \pmod n$.

### 2.6 Chinese Remainder Theorem (CRT)
* **Theorem:** If $\gcd(a, b) = 1$, then for any remainders $r_a \pmod a$ and $r_b \pmod b$, there exists a **unique** integer $n \pmod{ab}$ such that:
  $$n \equiv r_a \pmod a \quad \text{and} \quad n \equiv r_b \pmod b$$
* **Constructive Formula:**
  1. Find $x, y$ such that $ax + by = 1$ via Extended Euclid's Algorithm.
  2. Note that $by \equiv 1 \pmod a$ and $by \equiv 0 \pmod b$, while $ax \equiv 0 \pmod a$ and $ax \equiv 1 \pmod b$.
  3. Construct:
     $$n = (r_a \cdot b \cdot y + r_b \cdot a \cdot x) \bmod (ab)$$
* **Generalization:** Extends inductively to $k$ pairwise coprime moduli $m_1, m_2, \dots, m_k$, allowing big-integer arithmetic to be parallelized across smaller prime moduli.

### 2.7 Fast Modular Exponentiation
* **Goal:** Compute $b^e \bmod m$ without overflowing memory or performing $O(e)$ multiplications.
* **Binary Exponentiation (Repeated Squaring):**
  1. Express $e$ in binary: $e = \sum_{i=0}^{k} b_i 2^i$ where $b_i \in \{0, 1\}$.
  2. Iteratively square the base modulo $m$: $b^{2^0}, b^{2^1}, b^{2^2}, \dots, b^{2^k} \pmod m$.
  3. Multiply together the terms where $b_i = 1$.
* **Complexity:** Requires at most $2 \log_2 e$ modular multiplications ($\log_2 e$ squarings + at most $\log_2 e$ products).

### 2.8 Fermat's Little Theorem, Euler's Totient & Euler's Theorem
* **Fermat's Little Theorem (FLT):** If $p$ is prime and $p \nmid a$, then:
  $$a^{p-1} \equiv 1 \pmod p$$
  *(Equivalently, $a^p \equiv a \pmod p$ for all integers $a$.)*
  * **Optimization:** For prime $p$, $a^n \equiv a^{n \bmod (p-1)} \pmod p$.
* **Euler's Totient Function $\phi(n)$:** Counts the integers in $\{0, 1, \dots, n-1\}$ that are coprime to $n$.
  * For prime $p$: $\phi(p) = p - 1$.
  * For distinct primes $p, q$ (used in **RSA**): $\phi(pq) = (p - 1)(q - 1)$.
  * General formula: $\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$.
* **Euler's Theorem:** Generalizes FLT. If $\gcd(a, n) = 1$, then:
  $$a^{\phi(n)} \equiv 1 \pmod n$$

```text
Cycle Graph Proof of Euler's Theorem / FLT:
Multiplying coprime residues mod n by 'a' partitions all φ(n) residues into disjoint cycles of equal length l:

  r  --->  a·r  --->  a²·r  ---> ... ---> a^l·r ≡ r (mod n)   ===>  a^l ≡ 1 (mod n)
  r' --->  a·r' --->  a²·r' ---> ... ---> a^l·r' ≡ r' (mod n)

If there are 'c' disjoint cycles, then c · l = φ(n), so:
  a^φ(n) = a^(c·l) = (a^l)^c ≡ 1^c ≡ 1 (mod n)
```

---

## Day 2: Primes, Primality Testing & Conjectures

### 3.1 Infinitude of Primes (Multiple Proofs)
A **prime number** is a natural number $p > 1$ whose only positive divisors are $1$ and $p$. There are infinitely many primes, proven in diverse ways:
1. **Euclid's Proof:** Given a finite list $p_1, \dots, p_k$, $N = \prod_{i=1}^k p_i + 1$ has a prime factor not in the list. (Similarly, $n! + 1$ has a prime factor $> n$).
2. **Euler's Analytic Proof (Divergence of Harmonic Series):** If primes were finite, $\prod_p \frac{1}{1 - 1/p}$ would be finite, contradicting $\sum_{m=1}^\infty \frac{1}{m} = \infty$.
3. **Goldbach's Proof (Fermat Numbers):** Fermat numbers $F_n = 2^{2^n} + 1$ satisfy $F_m - 2 = F_0 F_1 \cdots F_{m-1}$. Since every $F_n$ is odd, $\gcd(F_n, F_m) = 1$ for $n \ne m$. Choosing one prime factor from each $F_n$ yields infinitely many distinct primes.
4. **Filip Saidak's Proof:** $N_1 = n(n+1)$ has $\ge 2$ prime factors; $N_2 = N_1(N_1 + 1)$ has $\ge 3$ prime factors; continuing inductively generates numbers with arbitrarily many distinct prime factors.
5. **Primes in Arithmetic Progressions:**
   * Form $4k + 3$: Consider $N = 4p_1p_2\cdots p_k - 1$.
   * Form $4k + 1$: Consider $N = (2p_1p_2\cdots p_k)^2 + 1$.
   * **Dirichlet's Theorem:** There are infinitely many primes of the form $ak + b$ iff $\gcd(a, b) = 1$.

### 3.2 Prime Number Theorem & Famous Conjectures
* **Prime Number Theorem (PNT):** Let $\pi(x)$ be the number of primes $\le x$. Asymptotically:
  $$\pi(x) \sim \frac{x}{\ln x}$$
* **Famous Conjectures & Results:**
  * **Goldbach's Conjecture:** Every even integer $> 2$ is the sum of two primes. *(Chen's Theorem proved every sufficiently large even integer is $p_1 + p_2 p_3$).*
  * **Twin Prime Conjecture:** There are infinitely many primes $p$ such that $p + 2$ is also prime.
  * **Legendre's Conjecture:** There is always at least one prime between $n^2$ and $(n+1)^2$.
  * **Euler's Prime-Generating Polynomial:** $f(n) = n^2 + n + 41$ produces primes for $0 \le n \le 39$, but fails at $n = 40$ ($40^2 + 40 + 41 = 41^2$). No non-constant single-variable polynomial can yield *only* primes.

### 3.3 Primality Testing & Sieve Methods
* **Sieve of Eratosthenes:** Lists integers from $2$ to $n$ and iteratively crosses out multiples of each prime $p \le \sqrt{n}$.
* **Trial Division & Wheel Factorization:**
  * Only need to test primes $p \le \sqrt{n}$.
  * **Wheel of 30:** Since $30 = 2 \times 3 \times 5$, any prime $> 5$ must be congruent to $\{1, 7, 11, 13, 17, 19, 23, 29\} \pmod{30}$, skipping $73.3\%$ of candidates.

### 3.4 Pseudoprimes, Carmichael Numbers & Advanced Tests
* **Fermat Pseudoprime (Base $a$):** A composite integer $n$ satisfying $a^{n-1} \equiv 1 \pmod n$.
  * *Example:* $341 = 11 \times 31$ is a pseudoprime to base $2$, but fails base $3$.
* **Carmichael Numbers:** Composite integers $n$ that are Fermat pseudoprimes for **every** base $a$ coprime to $n$ (i.e., $a^n \equiv a \pmod n$ for all $a$).
  * **Korselt's Criterion:** $n$ is a Carmichael number iff $n$ is composite, square-free, and $(p - 1) \mid (n - 1)$ for every prime $p \mid n$.
  * *Examples:* $561 = 3 \times 11 \times 17$, $1105$, $1729$ (Hardy-Ramanujan number), $2465$, $2821$.
* **Lucas Primality Test ($n-1$ Test):** $n > 1$ is prime if for every prime factor $q$ of $n - 1$, there exists an integer $a$ such that:
  $$a^{n-1} \equiv 1 \pmod n \quad \text{and} \quad a^{(n-1)/q} \not\equiv 1 \pmod n$$
  *(This proves $\text{ord}_n(a) = n - 1$, forcing $\phi(n) = n - 1$.)*
* **Lucas-Lehmer Test (for Mersenne Numbers):** Let $S_0 = 4$ and $S_k = S_{k-1}^2 - 2$. For an odd prime $p$, $M_p = 2^p - 1$ is prime **if and only if**:
  $$S_{p-2} \equiv 0 \pmod{2^p - 1}$$
  *(Used by Édouard Lucas in 1876 to prove $2^{127} - 1$ is prime—the largest prime ever calculated by hand!)*

### 3.5 Mersenne Primes, Perfect Numbers & Antiprimes
* **Mersenne Primes:** Primes of the form $M_n = 2^n - 1$. Necessary condition: $n$ itself must be prime (since $2^{ab} - 1$ is divisible by $2^a - 1$).
* **Perfect Numbers:** Positive integers equal to the sum of their proper positive divisors (e.g., $6, 28, 496, 8128$).
* **Antiprimes (Highly Composite Numbers):** Positive integers $n$ that have strictly more divisors $d(n) = \prod (a_i + 1)$ than any smaller positive integer ($1, 2, 4, 6, 12, 24, 36, 48, 60, \dots, 360$). Their prime factorizations always consist of consecutive primes starting at $2$ with non-increasing exponents ($a_1 \ge a_2 \ge \dots \ge a_k$).

---

## Day 1 Assignment: Python Implementation Solutions

Below are the complete, assertion-compliant Python solutions for `Day 1 Assignment.ipynb`.

### Problem 1: Extended Euclid's Algorithm
Calculates $(d, x, y)$ such that $d = \gcd(a, b) = ax + by$ for $a \ge b \ge 0$.

```python
def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    
    if b == 0:
        d, x, y = a, 1, 0
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - (a // b) * q
        
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

# Verification
print(extended_gcd(8, 4))    # Output: (4, 0, 1)
print(extended_gcd(27, 15))  # Output: (3, -1, 2)
```

### Problem 2: Least Common Multiple (LCM)
Computes $\text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$ using integer division.

```python
def lcm(a, b):
    assert a > 0 and b > 0
    d, _, _ = extended_gcd(max(a, b), min(a, b))
    return (a // d) * b

# Verification
assert lcm(9, 3) == 9
assert lcm(17, 37) == 629
```

### Problem 3: Linear Diophantine Equations
Finds $(x, y)$ such that $ax + by = c$, handling cases where $a < b$ safely.

```python
def diophantine(a, b, c):
    if a >= b:
        gcd, x0, y0 = extended_gcd(a, b)
    else:
        gcd, y0, x0 = extended_gcd(b, a)
        
    assert c % gcd == 0
    
    multiplier = c // gcd
    x = x0 * multiplier
    y = y0 * multiplier
    
    assert a * x + b * y == c
    return (x, y)

# Verification
print(diophantine(34, 51, 170))  # Output: (-10, 10) -> 34(-10) + 51(10) = 170
print(diophantine(91, 117, 65))  # Output: (20, -15) -> 91(20) + 117(-15) = 65
```

### Problem 4: Modular Multiplicative Inverse & Modular Division
Computes $a^{-1} \pmod n$ and returns $x \equiv b / a \pmod n$ with $0 \le x \le n - 1$.

```python
def modInverse(a, n):
    """Calculate the multiplicative inverse of a (mod n)"""
    if a >= n:
        d, x, _ = extended_gcd(a, n)
    else:
        d, _, x = extended_gcd(n, a)
        
    assert d == 1
    return x % n

def divide(b, a, n):
    assert n > 1 and a > 0
    aInv = modInverse(a, n)
    assert (a * aInv) % n == 1
    return (aInv * b) % n

# Verification
print(divide(9, 5, 3))      # Output: 0 (since 9 ≡ 0 mod 3)
print(divide(223, 67, 54))  # Output: 31 (since 67 * 31 = 2077 ≡ 223 mod 54)
```

### Problem 5: Fast Modular Exponentiation
Computes $b^e \bmod m$ in $O(\log_2 e)$ multiplications using binary exponentiation.

```python
def FastModularExponentiation(b, e, m):
    if m == 1:
        return 0
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        e //= 2
    return result

# Verification
print(FastModularExponentiation(4, 5, 3))  # Output: 1 (4^5 = 1024 ≡ 1 mod 3)
```

### Problem 6: Chinese Remainder Theorem (CRT)
Constructs the unique solution $r \in [0, n_1 n_2 - 1]$ satisfying $r \equiv r_1 \pmod{n_1}$ and $r \equiv r_2 \pmod{n_2}$.

```python
def ChineseRemainderTheorem(n1, r1, n2, r2):
    (d, x, y) = extended_gcd(n1, n2)
    assert d == 1
    
    mod = n1 * n2
    # Since n1*x + n2*y = 1:
    # r2*n1*x + r1*n2*y satisfies both congruences
    r = (r2 * n1 * x + r1 * n2 * y) % mod
    return r

# Verification
print(ChineseRemainderTheorem(13, 7, 6, 5))    # Output: 59
print(ChineseRemainderTheorem(28, 20, 19, 3))  # Output: 440
```

---

## Day 2 Assignment: Theoretical Proofs & Solutions

### Problem 1: Repunit Divisibility (Easy)
> **Statement:** Define $a(1) = 1, a(2) = 11, a(3) = 111, \dots, a(n) = \underbrace{11\dots1}_{n\text{ times}}$. Let $p$ be a prime and $A_p = \{n \in \mathbb{N} : p \mid a(n)\}$. Prove that $A_p = \emptyset$ if $p \in \{2, 5\}$, and $A_p$ is infinite for all other primes.  
> **Bonus:** For a given prime $p$, determine the exact set $A_p$.

#### Proof:
1. **Closed Form of $a(n)$:**
   Notice that $a(n)$ is a geometric series of powers of $10$:
   $$a(n) = 1 + 10 + 10^2 + \dots + 10^{n-1} = \frac{10^n - 1}{9}$$
2. **Case 1: $p = 2$ or $p = 5$:**
   Every term $a(n)$ ends with the digit $1$ in base $10$. Since a number is divisible by $2$ iff its last digit is even, and divisible by $5$ iff its last digit is $0$ or $5$, neither $2$ nor $5$ can ever divide $a(n)$. Hence, $A_2 = A_5 = \emptyset$.
3. **Case 2: $p = 3$:**
   The sum of the digits of $a(n)$ is $n$. By the divisibility rule for $3$, $3 \mid a(n) \iff 3 \mid n$. Thus, $A_3 = \{3k : k \in \mathbb{N}\}$, which is infinite.
4. **Case 3: All other primes $p \notin \{2, 3, 5\}$:**
   Since $\gcd(p, 9) = 1$, $p \mid \frac{10^n - 1}{9} \iff p \mid (10^n - 1) \iff 10^n \equiv 1 \pmod p$.
   Because $\gcd(p, 10) = 1$, **Fermat's Little Theorem** guarantees:
   $$10^{p-1} \equiv 1 \pmod p$$
   Therefore, for every positive integer $k \in \mathbb{N}$:
   $$10^{k(p-1)} = \left(10^{p-1}\right)^k \equiv 1^k \equiv 1 \pmod p$$
   Thus, $n = k(p-1) \in A_p$ for all $k \ge 1$, proving $A_p$ is infinite.

#### Bonus (Exact Set $A_p$):
* For $p \in \{2, 5\}$: $A_p = \emptyset$.
* For $p = 3$: $A_3 = \{3k : k \in \mathbb{N}\}$.
* For any prime $p > 5$: Let $d = \text{ord}_p(10)$ be the multiplicative order of $10$ modulo $p$ (the smallest positive integer $d$ such that $10^d \equiv 1 \pmod p$, where $d \mid p-1$). Then $10^n \equiv 1 \pmod p \iff d \mid n$. Hence:
  $$A_p = \{k \cdot \text{ord}_p(10) : k \in \mathbb{N}\}$$

---

### Problem 2: Euclid–Euler Theorem on Even Perfect Numbers (Moderate)
> **Statement:** Prove that an even integer $k$ is a perfect number if and only if $k = 2^{n-1}(2^n - 1)$ where $2^n - 1$ is prime.

#### Proof:
Let $\sigma(m)$ denote the sum of all positive divisors of $m$. By definition, $k$ is perfect iff $\sigma(k) = 2k$. Recall that $\sigma$ is a **multiplicative function** ($\sigma(ab) = \sigma(a)\sigma(b)$ whenever $\gcd(a, b) = 1$).

1. **($\Leftarrow$) Sufficiency:**
   Suppose $k = 2^{n-1}(2^n - 1)$ where $p = 2^n - 1$ is prime (note $n \ge 2$ since $p \ge 3$).
   Since $\gcd(2^{n-1}, p) = 1$:
   $$\sigma(k) = \sigma(2^{n-1}) \cdot \sigma(p) = \left(1 + 2 + 4 + \dots + 2^{n-1}\right)(1 + p) = (2^n - 1)(2^n) = 2 \cdot 2^{n-1}(2^n - 1) = 2k$$
   Thus, $k$ is an even perfect number.

2. **($\Rightarrow$) Necessity:**
   Suppose $k$ is an even perfect number. Write $k = 2^{n-1} m$ where $n \ge 2$ and $m$ is odd ($\gcd(2^{n-1}, m) = 1$).
   Since $k$ is perfect, $\sigma(k) = 2k = 2^n m$. Using multiplicativity of $\sigma$:
   $$2^n m = \sigma(2^{n-1} m) = \sigma(2^{n-1}) \sigma(m) = (2^n - 1)\sigma(m)$$
   Since $\gcd(2^n - 1, 2^n) = 1$, Euclid's Lemma implies $(2^n - 1) \mid m$. Thus, $m = c(2^n - 1)$ for some positive integer $c$.
   Substituting this back into the equation gives:
   $$2^n c(2^n - 1) = (2^n - 1)\sigma(m) \implies \sigma(m) = 2^n c$$
   Notice that $m$ and $c$ are both divisors of $m$ (with $c < m$ since $2^n - 1 \ge 3$). Therefore:
   $$\sigma(m) \ge m + c = c(2^n - 1) + c = 2^n c$$
   Equality holds **if and only if** $m$ has **no other positive divisors** besides $m$ and $c$. This forces $c = 1$ and $m = 2^n - 1$ to be prime. Hence $k = 2^{n-1}(2^n - 1)$ with $2^n - 1$ prime. $\blacksquare$

---

### Problem 3: Infinitude of Fermat Pseudoprimes Base $a$ (Hard)
> **Statement:** Prove that for each integer $a \ge 2$, there exist infinitely many composite integers $n$ such that $a^{n-1} \equiv 1 \pmod n$.

#### Proof:
We construct an infinite sequence of Fermat pseudoprimes base $a$ using the **Cipolla construction** (or cyclotomic factors of $a^{2p} - 1$).

1. **Construction of $n$:**
   Choose any odd prime $p$ such that $p \nmid a(a^2 - 1)$. (Since $a(a^2 - 1) \ne 0$ has finitely many prime factors, there are infinitely many such odd primes $p$.)
   Define:
   $$n = \frac{a^{2p} - 1}{a^2 - 1} = \left(\frac{a^p - 1}{a - 1}\right)\left(\frac{a^p + 1}{a + 1}\right)$$

2. **Proof that $n$ is Composite:**
   Since $a \ge 2$ and $p \ge 3$ is an odd prime:
   * First factor: $\frac{a^p - 1}{a - 1} = 1 + a + a^2 + \dots + a^{p-1} > 1 + 2 + 4 = 7 > 1$.
   * Second factor: $\frac{a^p + 1}{a + 1} = 1 - a + a^2 - \dots + a^{p-1} = (a^{p-1} - a^{p-2}) + \dots + (a^2 - a) + 1 \ge (2^2 - 2) + 1 = 3 > 1$.
   Since $n$ is the product of two integers strictly greater than $1$, **$n$ is composite**.

3. **Proof that $n - 1$ is Divisible by $2p$:**
   Compute $n - 1$:
   $$n - 1 = \frac{a^{2p} - 1}{a^2 - 1} - 1 = \frac{a^{2p} - a^2}{a^2 - 1} = \frac{a^2(a^{2(p-1)} - 1)}{a^2 - 1}$$
   * **Divisibility by $2$:**
     * If $a$ is even, $2 \mid a^2$. Since $p \nmid (a^2 - 1)$ and $a^2 - 1$ is odd, $\gcd(2, a^2 - 1) = 1$, so $2 \mid (n - 1)$.
     * If $a$ is odd, $n = 1 + a^2 + a^4 + \dots + a^{2(p-1)}$ is a sum of $p$ odd terms. Because $p$ is odd, $n$ is odd, so $n - 1$ is even ($2 \mid (n - 1)$).
   * **Divisibility by $p$:**
     Since $p \nmid a$, Fermat's Little Theorem gives $a^{p-1} \equiv 1 \pmod p \implies a^{2(p-1)} \equiv 1 \pmod p$, so $p \mid (a^{2(p-1)} - 1)$. Because we chose $p \nmid (a^2 - 1)$, we have $\gcd(p, a^2 - 1) = 1$, which implies $p \mid (n - 1)$.
   * Combining $\gcd(2, p) = 1$, we conclude $2p \mid (n - 1)$, i.e., $n - 1 = 2pk$ for some integer $k \ge 1$.

4. **Verification of Fermat's Congruence:**
   By definition of $n$, $(a^2 - 1)n = a^{2p} - 1$, which implies:
   $$a^{2p} \equiv 1 \pmod n$$
   Raising both sides to the $k$-th power:
   $$a^{n-1} = a^{2pk} = \left(a^{2p}\right)^k \equiv 1^k \equiv 1 \pmod n$$

5. **Infinitude:**
   Since $n = \frac{a^{2p} - 1}{a^2 - 1}$ is strictly increasing with $p$, and there are infinitely many odd primes $p \nmid a(a^2 - 1)$, this generates **infinitely many** distinct Fermat pseudoprimes base $a$. $\blacksquare$
