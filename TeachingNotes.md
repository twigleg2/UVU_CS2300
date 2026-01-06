# Lecture Notes for CS 2300 - Discrete Mathematics

## Lecture 2, Sections 1.1 - 1.3

### Proposition
- A statement that is either true or false
- often denoted with variables $p$, $q$, $r$
- compound propositions can be made by combining propositions with logical operators


### Logical operators
- $\neg$ : Negation, Not
- $\land$ : Conjunction, And
- $\lor$ : Disjunction, (inclusive) Or
- $\oplus$ : Exclusive Or
  - **Note**: The _Exclusive Or_ can be written as a combination of the other three operators, and therefore is not often written down in discrete mathematics.
  - **Practice**: How does the English language handle the difference between the _Inclusive Or_ and _Exclusive Or_?


#### Order of operations
1. $\neg$ , NOT
2. $\land$ , AND
3. $\lor$ , OR
   - Use parenthesis to change the order of operations, just like you would in algebra.
   - **Practice**: Why is the _Exclusive Or_ not in this list?


### Truth tables
- We often use truth tables to visually solve compound propositions
- The number of rows in a truth table is equal to $2^n$, where $n$ is the number of variables
- Example truth table:

$$
\begin{array}{|c c|c|}
\hline
p & q & p \land q \\
\hline
T & T & T \\
T & F & F \\
F & T & F \\
F & F & F \\
\hline
\end{array}
$$

- **Practice**: Make a truth table with three variables
- **Practice**: Make a truth table with columns for the intermediate calculations of a complex compound proposition


### Short circuiting a compound proposition
- Sometimes there is no need calculate all parts of a compound proposition.  When this happens, we call it a short-circuit.
- Example: $p \land (q \lor r \lor \neg t)$
  - If $p$ is false, we do not need to calculate the rest of the equation because the statement will be false regardless.
  - **practice**: Can you show a similar example that short-circuits on the $\lor$ operator?


### Conditional statements
- $p \to q$ : Conditional, Implication
  - Read: "if $p$ then $q$", "$p$ implies $q$", "$p$ only if $q$"
  - Check out table 1.3.2 in Zybooks for other ways you can express a conditional statement in English
- $p$ is called the hypothesis, $q$ is called the conclusion
- The statement $p \to q$ resolves to false only when the hypothesis $p$ is true and the conclusion $q$ is false.
- Importantly, this relationship does not go the other direction!  $q$ has no influence over $p$.  This is why when $p$ is false and $q$ is true, the statement still resolves to true
  - ex. If you don't turn in your homework on time, then you will not score 100% on that assignment.
  - Turning in your homework on time does not guarantee you will score 100%.  There are many other ways to not score 100%, and so your score being less than 100% says nothing about when you turned it in.
  - **Practice**: Apply the same logic to the statement "If I get stuck in traffic, then I will be late for class"

$$
\begin{array}{|cc|c|}
\hline
p & q & p \rightarrow q \\
\hline
T & T & T \\
T & F & F \\
F & T & T \\
F & F & T \\
\hline
\end{array}
$$

- $p \to q$ is logically equivalent to $\neg p \lor q$
  - **Practice**: Draw the truth table for both of these to prove it to yourself


#### Related statements
- Inverse: $\neg p \to \neg q$
- Converse: $q \to p$
- Contrapositive: $\neg q \to \neg p$
  - The _Contrapositive_ is logically equivalent to the original conditional statement.  The _Inverse_ and _Converse_ are not, but they are logically equivalent to each other.


### Biconditional statement
- $p \leftrightarrow q$ : Biconditional, equivalence
  - Read: "$p$ if and only if $q$", "$p$ is equivalent to $q$"
    - "If and only if" is often abbreviated as "iff"
- $p \leftrightarrow q$ is logically equivalent to $(p \to q)\land(q \to p)$
  - In other words, $p$ and $q$ must have the same value, or the statement is false


#### Order of operations with Conditional and Biconditional statements
1. $\neg$ , NOT
2. $\land$ , AND
3. $\lor$ , OR
4. $\to$ Conditional  ; $\leftrightarrow$ Biconditional

- Note: If there are more than one _Conditional_ and/or _Biconditional_ statements, they are applied in right-to-left order, which is often unintuitive.  It's best practice to use parenthesis to be explicit about the order in which operations should be performed.


## Lecture 3, Sections 1.4 - 1.5

### Tautology
- A compound proposition that is always true, no matter what.
- ex. $p \lor \neg p$


### Contradiction
- A compound proposition that is always false, no matter what
  - ex. $p \land \neg p$


### Contingent
- A compound proposition that could be either true or false
  - **practice**: Are the following a _Tautology_, a _Contradiction_, or _Contingent_?
  - $p \leftrightarrow \neg p$
  - $p \to p$
  - $\neg p \to \neg p$
  - $p \to \neg p$
  - $(p \land q) \to p$


### Logical equivalence
- $\equiv$ 
- This symbol inserted in between two statements denotes that those two statements are logically equivalent.
- Two statements that are logically equivalent may be used to substitute for each other in a complex compound proposition
  - When doing a substitution, always use parenthesis to avoid errors with the order of operations
- To demonstrate logical equivalence, build a truth table and compare the columns for each statement
- **Practice**: Look at the exercises at the bottom of section 1.4 in Zybooks.
- **Practice**: Ask an AI chat bot to generate two (complex) compound propositions.  Then determine if they are or are not logically equivalent by drawing a truth table.


### De Morgan's Law
- Negation of Conjunction
  - $\neg(p \land q) \equiv \neg p \lor \neg q$
- Negation of Disjunction
  - $\neg (p \lor q) \equiv \neg p \land \neg q$
- **Practice**: Draw the truth tables to show they are logically equivalent


### Other laws of propositional logic

| Law | | |
| --- | --- | --- |
| Double negation | $\neg \neg p \equiv p$ | |
| Complement | $\neg F \equiv T$ | $\neg T \equiv F$ |

| Law | $\lor$ version | $\land$ version |
| --- | --- | --- |
| Complement (cont.) | $p \lor \neg p \equiv T$ | $p \land \neg p \equiv F$ |
| Identity | $p \lor F \equiv p$ | $p \land T \equiv p$ |
| Domination | $p \lor T \equiv T$ | $p \land F \equiv F$ |
| Idempotent | $p \lor p \equiv p$ | $p \land p \equiv p$ |
| Commutative | $p \lor q \equiv q \lor p$ | $p \land q \equiv q \land p$ |
| Associative | $p \lor (q \lor r) \equiv (p \lor q) \lor r$ | $p \land (q \land r) \equiv (p \land q) \land r$ |
| Distributive | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ | $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ |
| De Morgan's | $\neg (p \lor q) \equiv \neg p \land \neg q$ | $\neg(p \land q) \equiv \neg p \lor \neg q$ |
| Absorption | $p \lor (p \land q) \equiv p$ | $p \land (p \lor q) \equiv p$ |

| Conditional Identities |
| --- |
| $p \to q \equiv \neg p \lor q$ |
| $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$ |

- **Practice**: Prove the absorption laws, then do some exercises from section 1.5

## Lecture 4, Sections 1.6 - 1.8


## Lecture 5, Sections 1.9 - 1.10


## Lecture 6, Sections 2.1 - 2.3


## Lecture 7, Sections 2.4 - 2.6


## Lecture 8, Sections 2.7 - 2.10


## Lecture 9, Midterm 1 Review


## Lecture 10, Sections 3.1 - 3.4


## Lecture 11, Sections 3.5 - 3.7


## Lecture 12, Sections 4.1 - 4.3


## Lecture 13, Sections 4.4 - 4.6


## Lecture 14, Sections 5.1 - 5.3


## Lecture 15, Sections 5.4 - 5.6


## Lecture 16, Sections 5.7 - 5.9


## Lecture 17, Sections 6.1 - 6.5


## Lecture 18, Sections 7.1 - 7.5


## Lecture 19, Midterm 2 Review


## Lecture 20, Sections 8.1 - 8.3


## Lecture 21, Sections 8.4 - 8.6


## Lecture 22, Sections 8.8 - 8.9


## Lecture 23, Sections 8.10 - 8.11


## Lecture 24, Sections 9.1 - 9.4


## Lecture 25, Sections 9.5 - 9.8


## Lecture 26, Sections 9.9 - 9.12


## Lecture 27, Sections 9.13 - 9.15


## Lecture 28, Final Exam Review
