# Lecture Notes for CS 2300 - Discrete Mathematics

## Lecture 1

Read the syllabus  
Study LaTex

## Lecture 2
Sections 1.1 - 1.3

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
  - if $p$ then $q$
  - $p$ implies $q$
  - $p$ only if $q$
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
  - $p$ is equivalent to $q$
  - $p$ if and only if $q$
    - "If and only if" is often abbreviated as "iff"
- $p \leftrightarrow q$ is logically equivalent to $(p \to q)\land(q \to p)$
  - In other words, $p$ and $q$ must have the same value, or the statement is false


#### Order of operations with Conditional and Biconditional statements
1. $\neg$ , NOT
2. $\land$ , AND
3. $\lor$ , OR
4. $\to$ Conditional  ; $\leftrightarrow$ Biconditional

- Note: If there are more than one _Conditional_ and/or _Biconditional_ statements, they are applied in right-to-left order, which is often unintuitive.  It's best practice to use parenthesis to be explicit about the order in which operations should be performed.


## Lecture 3
Sections 1.4 - 1.5

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


## Lecture 4
Sections 1.6 - 1.8

### Predicate
- A logical statement with a truth value that is a function (of one or more variables).  That is to say, the truth value of the statement is dependent on the value of the variables ($x$, $y$, etc.).
  - $P(x) : x > 0$
    - $x$ is positive
  - $P(x,y) : x = y$
    - $x$ is equal to $y$
- A predicate turns into a proposition after all of it's variables are assigned a value.
  - $P(5) : x \bmod 2 = 0$  
    - 5 is even, which is a false proposition


### Quantified Statements
- We can also turn a predicate into a proposition by considering all possible values (of x, y, etc.).
- When evaluating a _quantified statement_, we must first chose a **domain**, or a set of possible values, to test against.  
  - example domains:
    - positive numbers
    - rational numbers
    - students in the class


#### Universally Quantified Statement
- $\forall$ : Universal Quantifier
- $\forall x P(x)$
  - For all $x$, $P(x)$
- For a domain of size $n$, this is equivalent to:
  - $P(x_1) \land P(x_2) \land ... \land P(x_n)$
- A _universally quantified statement_ is false if there exists one or more _Counterexamples_.
- A **Counterexample** is one value from the domain that proves the _universally quantified statement_ false.
  - If the domain is empty, the _universally quantified statement_ is true, because there does not exist a counterexample.


#### Existentially Quantified Statement
- $\exists$ : Existential Quantifier
- $\exists x P(x)$
  - there exists an $x$, such that $P(x)$
- For a domain of size $n$, this is equivalent to:
  - $P(x_1) \lor P(x_2) \lor ... \lor P(x_n)$
- An _existentially quantified statement_ is true if there exists one or more _Examples_.
- An **example** is one value from the domain that proves the _existentially quantified statement_ true.
  - If the domain is empty, the _existentially quantified statement_ is false, because an _example_ does not exist.


### Compound Quantified Statements
- We can combine quantified statements with logical operators to create compound quantified statements
  - Example: $\forall x(P(x) \land Q(x))$
    - $x$ is a student
    - $P(x)$ : $x$ studies
    - $Q(x)$ : $x$ passes the exam
    - All students who study pass the exam


### De Morgan's law for quantified statements
- Negation of universally quantified statements:
  - $\neg \forall x P(x) \equiv \exists x \neg P(x)$
- Negation of existentially quantified statements:
  - $\neg \exists x P(x) \equiv \forall x \neg P(x)$


## Lecture 5
Sections 1.9 - 1.10

### Nested Quantifiers
We can combine universal and/or existential quantifiers  

- $\forall x \exists y P(x,y)$
  - $x$ is a student in the class
  - $y$ is a desk in the classroom
  - $P(x,y)$ : $x$ sits at $y$
  - For all students in the class, there exists a desk in the classroom to sit at.  That is to say, each student sits at their own desk.

Note that swapping the order of two different quantifiers changes the meaning (adjacent quantifiers of the same type can be swapped without consequence).  

- $\exists y \forall x P(x,y)$
  - There exists a desk in the classroom for all students in the class to sit at.  That is to say, all students sit at the same desk.


### De Morgan's law for nested quantified statements
- Every time the negation passes by a quantifier, change it's type
  - $\neg \forall x \exists y \exists z P(x,y,z) \equiv$
  - $\exists x \neg \exists y \exists z P(x,y,z) \equiv$
  - $\exists x \forall y \neg \exists z P(x,y,z) \equiv$
  - $\exists x \forall y \forall z \neg P(x,y,z)$


### Expressing "everyone else"
Imagine the following scenario:
- $\forall x \forall y P(x,y)$
- "Every team member gave a high-five to everyone"
  - Note that the domain for $x$ and $y$ is the same.  That is, we only have a single team of people.

As it stands now, this statement means that everyone also gave a high-five to themselves, which is probably not what we intended.
We Probably meant to say "Every team member gave a high-five to everyone else" or "Every team member gave a high-five to every other team member.
We can modify our statement in two ways to get closer to our intent:
- $\forall x \forall y (x \neq y \to P(x,y))$
  - In this case, each team member may or may not have given themselves a high five; we don't care either way.
- $\forall x \forall y (x \neq y \land P(x,y))$
  - In this case, each team member definitely did not give themselves a high five.


### Expressing "uniqueness"
How would you express the following in a logical statement?

- Only one student skipped class

We can't simply write $\exists x P(x)$, because this wold mean that one _or more_ students skipped class.  To check for uniqueness, we have to modify our statement:

- $\exists x (P(x) \land \forall y (x \neq y \to \neg P(y)))$

**Practice**: Break this down into parts to demonstrate why this works


### Quantifier Distribution
Remember that the universal quantifier $\forall$ acts like a long sting of conjunction $\land$ operations, and the existential quantifier $\exists$ acts like a long sting of disjunction $\lor$ operations.  Because of this, the universal quantifier can be distributed over conjunctions $\land$ and the existential quantifier can be distributed over disjunctions $\lor$.

Examples:
- $\forall x (P(x) \land Q(x)) \equiv \forall x P(x) \land \forall x Q(x)$
- $\exists x (P(x) \lor Q(x)) \equiv \exists x P(x) \lor \exists x Q(x)$


### Scope shifting
If a statement (conjunction or disjunction) does not contain a variable bound by a quantifier, it can be pulled into or out of that quantifier

Examples:
- $\forall x (\exists y Q(y)\land P(x)) \equiv \forall x \exists y (P(x) \land Q(y))$

This can also be done with the implication $\to$, but be careful you do it correctly!  Convert it to the form $\neg p \lor q$ using the conditional identify first to make sure you don't make a mistake.  For most, this is very unintuitive and easy to mess up.

## Lecture 6
Sections 2.1 - 2.3

### Arguments

An argument takes the logical statements that we are familiar with and writes them in a new form, with hypotheses (or **premises**) on top and the conclusion on the bottom.  

$$
\begin{aligned}
& p \to q \\
& p \\
& \overline{\therefore q} \\
\end{aligned}
$$

- $\therefore$ This symbol means "therefore"
- $p \to q$ is a hypothesis
- $p$ is a hypothesis
- $q$ is the conclusion

Arguments can also be written in english:  

If I have completed my homework, then I will turn it in  
I have completed my homework  
$\therefore$ I will turn it in


#### Valid Arguments
We can show that an argument is valid or not by drawing a truth table.  To do this, we check all cases where all hypotheses are true:

- If the conclusion is true in each case, the argument is valid.
- If the conclusion is false in one or more cases, the argument is invalid.

We can skip or ignore any case where one or more hypotheses are false, because validity assumes the hypotheses are true.

#### Practice
Are the following Valid or Invalid arguments? Use a truth table.

$$
\begin{aligned}
& p \to q \\
& p \\
& \overline{\therefore q} \\
\end{aligned}
$$

$$
\begin{aligned}
& r \land s \\
& r \to \neg s \\
& \overline{\therefore \neg r \to s}
\end{aligned}
$$

$$
\begin{aligned}
& p \to q \\
& \neg p \to \neg q \\
& \overline{\therefore q \to p}
\end{aligned}
$$

##### Footnote

Arguments can be rewritten by conjoining the premises and implying the conclusion.  The first practice problem above can be rewritten as:
- $((p \to q) \land p) \to q$

If this statement is a tautology, then the argument is valid.


### Rules of inference

#### Common valid arguments

| Rule                       | Example                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Modus Ponens**           | $P \rightarrow Q$<br>$P$<br>$\overline{\therefore\ Q}$                             |
| **Modus Tollens**          | $P \rightarrow Q$<br>$\neg Q$<br>$\overline{\therefore\ \neg P}$                   |
| **Addition**               | $P$<br>$\overline{\therefore\ P \lor Q}$                                           |
| **Simplification**         | $P \land Q$<br>$\overline{\therefore\ P}$                                          |
| **Conjunction**            | $P$<br>$Q$<br>$\overline{\therefore\ P \land Q}$                                   |
| **Hypothetical Syllogism** | $P \rightarrow Q$<br>$Q \rightarrow R$<br>$\overline{\therefore\ P \rightarrow R}$ |
| **Disjunctive Syllogism**  | $P \lor Q$<br>$\neg P$<br>$\overline{\therefore\ Q}$                               |
| **Resolution**             | $P \lor Q$<br>$\neg P \lor R$<br>$\overline{\therefore Q \lor R}$                  |

### Example Solution
Given the following argument, we can show it is valid in more than one way:

$$
\begin{aligned}
& (a \lor b) \to (c \lor d) \\
& \neg c \\
& \neg d \\
& \overline{\therefore \neg a} \\
\end{aligned}
$$

| Step | Statement                   | Rule Used          |
| ---: | -------------------------   | ------------------ |
|    1 | $(a \lor b) \to (c \lor d)$ | Hypothesis         |
|    2 | $\neg c$                    | Hypothesis         |
|    3 | $\neg d$                    | Hypothesis         |
|    4 | $\neg c \land \neg d$       | Conjunction, 2,3   |
|    5 | $\neg(c \lor d)$            | De Morgan's Law, 4 |
|    6 | $\neg(a \lor b)$            | Modus Tollens, 1,5 |
|    7 | $\neg a \land \neg b$       | De Morgan's Law, 6 |
|    8 | $\neg a$                    | Simplification, 7  |

| Step | Expression                                                                             | Law Used                    |
| ---: | -----------------------------------------------------------------------------------    | --------------------------- |
|    1 | $\big(((a \lor b) \to (c \lor d)) \land \neg c \land \neg d \big) \to \neg a$          | Given Statement             |
|    2 | $\neg\big((a \lor b) \to (c \lor d) \land \neg c \land \neg d \big) \lor \neg a$       | Implication Identity        |
|    3 | $\neg\big((\neg(a \lor b) \lor (c\lor d)) \land \neg c \land \neg d \big) \lor \neg a$ | Implication Identity        |
|    4 | $\big(\neg(\neg(a \lor b) \lor (c\lor d)) \lor c \lor d \big) \lor \neg a$             | De Morgan’s Law             |
|    5 | $\big((a \lor b) \land \neg(c\lor d) \lor c \lor d \big) \lor \neg a$                  | De Morgan + Double Negation |
|    6 | $\big((a \lor b) \land (\neg c \land \neg d) \lor c \lor d \big) \lor \neg a$          | De Morgan’s Law             |
|    6 | $\big((a \lor b) \land (\neg d \land \neg c) \lor c \lor d \big) \lor \neg a$          | Commutative Law             |
|    7 | $\big((((a \lor b) \land \neg d) \land \neg c) \lor c \lor d \big) \lor \neg a$        | Associative Law             |
|    8 | $\big(((a \lor b) \land \neg d) \lor c \land \neg c \lor c \lor d \big) \lor \neg a$   | Distributive Law            |
|    9 | $\big(((a \lor b) \land \neg d) \lor c \land \top \lor d \big) \lor \neg a$            | Complement Law              |
|   10 | $\big(((a \lor b) \land \neg d) \lor c \lor d \big) \lor \neg a$                       | Identity Law                |
|   11 | $\big(((a \lor b) \land \neg d) \lor d \lor c \big) \lor \neg a$                       | Commutative Law             |
|   12 | $\big(((a \lor b) \lor d) \land \neg d\lor d \lor c \big) \lor \neg a$                 | Distributive Law            |
|   13 | $\big(((a \lor b) \lor d) \land \top \lor c \big) \lor \neg a$                         | Complement Law              |
|   14 | $\big(((a \lor b) \lor d) \lor c \big) \lor \neg a$                                    | Identity Law                |
|   15 | $(a \lor \neg a)\lor b \lor c \lor d$                                                  | Associative & Commutative   |
|   16 | $\top \lor b \lor c \lor d$                                                            | Complement Law              |
|   17 | $\top$                                                                                 | Domination Law              |

| $a$ | $b$ | $c$ | $d$ | $a\lor b$ | $c\lor d$ | $(a\lor b)\to(c\lor d)$ | $\neg c$ | $\neg d$ | All premises | $\neg a$ |
| :-: | :-: | :-: | :-: | :-------: | :-------: | :---------------------: | :------: | :------: | :----------: | :------: |
|  T  |  T  |  T  |  T  |     T     |     T     |            T            |     F    |     F    |       F      |     F    |
|  T  |  T  |  T  |  F  |     T     |     T     |            T            |     F    |     T    |       F      |     F    |
|  T  |  T  |  F  |  T  |     T     |     T     |            T            |     T    |     F    |       F      |     F    |
|  T  |  T  |  F  |  F  |     T     |     F     |          **F**          |     T    |     T    |       F      |     F    |
|  T  |  F  |  T  |  T  |     T     |     T     |            T            |     F    |     F    |       F      |     F    |
|  T  |  F  |  T  |  F  |     T     |     T     |            T            |     F    |     T    |       F      |     F    |
|  T  |  F  |  F  |  T  |     T     |     T     |            T            |     T    |     F    |       F      |     F    |
|  T  |  F  |  F  |  F  |     T     |     F     |          **F**          |     T    |     T    |       F      |     F    |
|  F  |  T  |  T  |  T  |     T     |     T     |            T            |     F    |     F    |       F      |     T    |
|  F  |  T  |  T  |  F  |     T     |     T     |            T            |     F    |     T    |       F      |     T    |
|  F  |  T  |  F  |  T  |     T     |     T     |            T            |     T    |     F    |       F      |     T    |
|  F  |  T  |  F  |  F  |     T     |     F     |          **F**          |     T    |     T    |       F      |     T    |
|  F  |  F  |  T  |  T  |     F     |     T     |            T            |     F    |     F    |       F      |     T    |
|  F  |  F  |  T  |  F  |     F     |     T     |            T            |     F    |     T    |       F      |     T    |
|  F  |  F  |  F  |  T  |     F     |     T     |            T            |     T    |     F    |       F      |     T    |
|  F  |  F  |  F  |  F  |     F     |     F     |            T            |     T    |     T    |     **T**    |   **T**  |


### Rules of Inference with Quantifiers
We cannot apply the rules of inference from above to quantified statements.  However, we can eliminate the quantifiers by taking an element from the domain and plugging it into the quantified variable.  ex:

- The domain is students from the class.
- $\forall x (P(x))$
- Joe is a student in the class
- $P(\text{Joe})$

Now, we can use $P(\text{Joe})$ with the rules of inference from above.  This is an example of _Universal Instantiation_.  

There are four rules of inference for quantified statements:

| Rule | Name |
| ---- | ---- |
| $c$ is _any_ element from the domain<br>$\forall x P(x)$<br>$\overline{\therefore P(c)}$ | Universal Instantiation |
| $c$ is an _arbitrary_ element from the domain<br>$P(c)$<br>$\overline{\therefore \forall x P(x)}$ | Universal Generalization |
| $\exists x P(x)$<br>$\overline{\therefore P(c) \land (c}$ is a _particular_ element from the domain$)$ | Existential Instantiation* |
| $c$ is _any_ element from the domain<br>$P(c)$<br>$\overline{\therefore \exists x P(x)}$ | Existential Generalization |

#### Arbitrary and Particular elements
- **Arbitrary elements** have no special properties other than the ones shared by all elements of a domain.
  - Ex. If the domain is humans and their dogs, then an arbitrary element has a heartbeat and breathes air.
- **Particular elements**  may have special properties that aren't shared by all other elements of the domain.
  - Ex. If the domain is humans and their dogs, then Joe is a particular element (with two thumbs).
  - *NOTE: If you use _Existential Instantiation_, you CAN NOT use a _particular_ element that has already been defined!  It must be newly named element.
  - Particular elements are often given as part of the hypothesis.  

At any point during a proof, you can define a new arbitrary or particular element on a new line.  ex:

| Rule | Name |
| ---- | ---- |
| $k$ is an _arbitrary_ element | element definition |
| Joe is a _particular_ element | element definition |


### Invalid Arguments with Quantifiers
To show that an argument which uses quantifiers is invalid, you can define a domain that causes all the hypotheses to be true and the conclusion to be false.  Create a table with the predicates along the top and the domain elements on the left, then assign each cell the appropriate truth value that makes the argument invalid. ex:

$$
\begin{aligned}
& \exists x P(x) \\
& \exists x Q(x) \\
& \overline{\therefore \exists x(P(x) \land Q(x))}
\end{aligned}
$$

| | $P$ | $Q$ |
| - | --- | --- |
| c | $T$ | $F$ |
| d | $F$ | $T$ |

- $\exists x P(x)$ is true, because c is $T$ in the $P$ column
- $\exists x Q(x)$ is true, because d is $T$ in the $Q$ column
- $\exists x(P(x) \land Q(x))$ is false, because there is no no row where both $P$ and $Q$ are $T$.

## Lecture 7
Sections 2.4 - 2.6

### Mathematical definitions
Read Zybooks section 2.4 if you need a refresher.

### Theorems
A theorem is a statement that can be proven true.  A proof might contain _axioms_ which are statements that are assumed to be true.  Most theorems are concerned with all elements in a domain (universal quantifier).

### Proofs of universal statements

#### Proof by exhaustion
It might be possible to prove a theorem by testing all elements in a domain if the domain is small enough (or you have enough computing power).  We do this by listing out all members of a domain and assigning them one at a time to a variable to test.

$n \in \{-1,0,1\} \to n^2 = |n|$

the $\in$ symbol means "element of".  So in this example, if $n$ is an element of the domain {-1, 0,1 }, then $n^2 = |n|$.  We can very prove this true by testing all elements in this domain because it contains only three elements.  However, if we added another element to the domain, it might no longer be true.

#### Proof by universal generalization

Many proofs are concerned with a domain the is infinitely large (or at least too large to check every element).  In this case, we need to use _Universal Generalization_ (see Rules of Inference with Quantifiers above).  Begin by naming an arbitrary element in the domain, and then prove the statement for that arbitrary element.  Because it's arbitrary and it shares all of its characteristics with all other elements in the domain, this is sufficient to prove the statement true for all elements in the domain.

**Note**: We cannot prove a universal statement by finding a single example that satisfies the statement, because that particular element may not share all of its properties with all other elements in the domain.

#### Counterexamples

As before, we can disprove a universal statement by providing a single counterexample.  In other words, we can find a _particular element_ from the domain that shows the statement is false.

For conditional statements, $\to$, a counterexample must satisfy _all_ hypotheses (premises) and contradict the conclusion.  If the particular element does not satisfy all hypotheses and also contradict the conclusion, then it is not a counterexample.


### Proofs of existential statements

#### constructive proof of existence
As before, we can prove an existential statement by providing an example (a particular element) that satisfies the statement.  This is called a _constructive proof of existence_.  

#### nonconstructive proof of existence

We can also prove it with a _nonconstructive proof of existence_, which does not provide an example.  One way to do this would be to show that the existence of an element without the required properties would cause a contradiction.  There are many other ways to form a nonconstructive existence proof.

#### Disproving existential statements

To disprove an existential statement (i.e. $\neg \exists x$), we would need to consider all elements of the domain.  If we use De Morgan's law to change the existential quantifier to a universal quantifier, then the proof uses _universal generalization_, as above.  
ex: $\neg \exists x P(x) \equiv \forall x \neg P(x)$

### Tips and Tricks

1. Statements:
   - A statement cannot be both true and not true at the same time.  Therefore, if you can prove that the negation of the statement is true ($\neg P \equiv T$), then the original statement must be false ($P \equiv F$).
2. Arguments (assume all premises are true):
   - If assuming the _negation_ of the conclusion is true leads to a contradiction, then the argument must be valid.
   - If assuming the _negation_ of the conclusion is true leads instead to a counterexample (that is, a situation where the premises are satisfied but the conclusion is false), then the argument is invalid.

## Lecture 8
Sections 2.7 - 2.10


## Lecture 9
Midterm 1 Review


## Lecture 10
Sections 3.1 - 3.4


## Lecture 11
Sections 3.5 - 3.7


## Lecture 12
Sections 4.1 - 4.3


## Lecture 13
Sections 4.4 - 4.6


## Lecture 14
Sections 5.1 - 5.3


## Lecture 15
Sections 5.4 - 5.6


## Lecture 16
Sections 5.7 - 5.9


## Lecture 17
Sections 6.1 - 6.5


## Lecture 18
Sections 7.1 - 7.5


## Lecture 19
Midterm 2 Review


## Lecture 20
Sections 8.1 - 8.3


## Lecture 21
Sections 8.4 - 8.6


## Lecture 22
Sections 8.8 - 8.9


## Lecture 23
Sections 8.10 - 8.11


## Lecture 24
Sections 9.1 - 9.4


## Lecture 25
Sections 9.5 - 9.8


## Lecture 26
Sections 9.9 - 9.12


## Lecture 27
Sections 9.13 - 9.15


## Lecture 28
Final Exam Review
