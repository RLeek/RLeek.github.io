^Unpublished

- beautiful types:
	- Effortful types
	- Types to encode validation/only valid statess
	- Types to encode proofs/contracts
	- Types to encode optionality/branching
	- Compositing types
	- Type orderings
	- 


- Types to encode work done
- Types to enforce contracts
- Types to encode explicit states
- Effortful types
- Compositing/ordering types
- Mapping types
- Subset types


- To encode properties
- To encode more values
- To encode less values


- types as immutable data structures





Code complete 2nd Edition
Generic ideas that are probably smart:
- Read-only objects vs write/read-only objects
- Sometimes it makes sense to turn a write/read-only object into a read-only object depending on where/how it is used

- A method/class should always work at the same level of abstraction, such that you don't need to know any more specific details. You only need to look at a subset of methods, not all of them
- Complexity is managed when you have a single source of truth/coupling as a means of enforcing since truth or uniformity
- Avoid primitives, as these often also expose unncessary details, - instead use custom types that also remove things the programmer doesn't know.
	- Hiding complexity is important


- Heuristics:
	- Find real-world objects
	- Form consistent abstractions
	- Encapsulate implementation details
	- Inherit- When inheritance simplifies design
	- Hide-secrets
	- Identify areas likely to change
		- Determine the minimum a user needs to know(i.e. least likely to change or hardest to change) 
	- Reduce coupling:
		- E.g. If you pass in a lot of variables then that is practically an implementation detail ( also causes coupling )
		- Make it easy to call a 

- Other heuristics
	- Build hiearchies
	- Assign responsiblities
	- Choose binding(assignment) time consciously
	- Make central points of control
	- Imagine your design as a series of black boxes
	- Use brute force-solution

- Design practices:
	- Iterate
	- Divide and conquer
	- Top-down and bottom-up approaches
	- Prototyping 

- THink about it in terms of objects
- Think about it in terms of information hiding:
	- What does this class need to hide to reduce complexity?

- Designing proper interfaces:
	- Design ADTs first
	- Group opposites together (consider if every operation has an opposite or not)
	- Use programmatic as opposed to semantic rules:
			- Rules enforced by the compiler rather than comments or names
	- Don't break abstraction (ensure everything works at the same level)
	- Minimize accessibility or rather "what best preserves the integrity of the interface abstraction", but hiding more > hiding less

	- Be wary of semantic violations of encapsulation:
		- Anytime you find yourself looking at a classes implementation to figure out how to use a class you're not programming to an interface, you're programming through an interface to the implementation

	- Keep the number of methods that a class calls to a minimum <- This is statistically correlated with a higher error rate.



- Several reasons to create a class:
	- Model real-world objcts
	- Model abstract objets
	- Reduce complexity <- a class should be used to hide some kind of information
	- Islate complexity <
	- Hide implementation details
	- Limit effects of changes
			- Understand areas most likely to change
	- Make central point of control
	- Facilitate reusable code:
			- Don't design for reuse - rather go through a project afterwards and determine what should be reusable.
	- Use packages, namespaces or header files to also combine related operations


- Naming convetions for functions:
	- When mapping/converting between two things say:
		- _measurement1_to_measurement2_
		- 

Designing routines:
	- Focus on cohesion:
		- A function that is pure is more likely to be cohesive
		- Functional cohesion: This is when a routine perfors one and only one coesion
			- e.g. sin(), GetCustomerName()
		- Sequential chesion: This is when a routine contains operations that must be performed in a specific order, that share data from step to step, but don't make up a complete function when done together
			- Often times these operations should be functions themselves
		- Communicational cohesion: This is when operations make use of the same data but aren't related in any other ways
			- Ideally convert these so each is their own separate function
		- Temporal cohestion: These are operations that are combined because they occur at the same time
			- These functions should call other functions to do operations
			- It is an 'orchestrator' so to speak

		- Procedural cohesion: This is where operations are done in a specified order, 

		- Logical cohesion: This is where logic is used to join cohesions such as a case stetament, it is reasonable if code consists solely of if/case statements

		- Coincidental cohesion: This is where there is no relatioship


- Good routine names:
	- Describe everything the routine does
		- If this is too complex, then this is a sign that you need to change things.

	- To name a function, use a description of the return value. e.g.
		- isReady(), next(), currentcolour()
	- To name a procedure, use a verb followed by an object e.g. PrintDocument(), 
	CalcMonthlyRevenues(), CheckOrderInfo, RepaginateDocument()
		- Procedures usually perform an operation on an object

	- Use opposites prcesily: Naming convetions for opposites helps consistency and readability
	- Establish convestions for common operations:


- Optimal routine lines:
	- just try to keep it lower than 200 lines, but there is no evidece that line sizes actually matters, consider other factors first when splitting lines



- Error handling:
	- This is a tradeoff between robustnes vs correctness, correctness means return no result rather than a wrong result, whilst robustness means returning a result is better than no result. 
	- Assertions should be used for states that should never occur, other tecniques for sttes that have to be handled
	- When throwing exceptions make sure they don't violate encapsulation (i.e. are at the same level of abstraction)
	- There is little conventional wisdom for how to handle issues
	- Define boundaries within a program, such that some subset of classes deal with dirty data and some subset of classes deal with clean data
		- There may be multiple layers of classes that handle dirty data
		- Convert input data to the proper form as soon as possible after its input
		- This can also be done at a class level, have a public method that does validation and handles dirty data and a private method that assumes data is clean (<- this is pretty clever)
		- This makes when to use assertions vs error handling obvious:
			- Dirty data classes use error handling, whilst clean data classes use assertions

	- Offensive coding: This refers to making sure that when errors occur they are obvious as possible. E.g. Detect memory allocation errors by filling memory etc. 


- Psuedocode:
	- Good psuedocode should be convertable to comments for a program
	- Design -> psuedocode -> code (this ensures you catch high level errors first, followed by medium level errors, followed by low-level errors)
	- Design the routine: Should include 
		- Information it will hide
		- Inputs to the routine
		- Outputs from the routine
		- Preconditions that should be true for the routine
		- Postconditions that should be true after the routine runs
		- Name the routine (good naming indicates good code, bad naming indicates bad code)
		- Decide how to test the routine
		- Think about everything that could go wrong
		- Think about efficiency 

	- Write the pseudocode:
		- Go from most general to most specific:
		- Begin with header that describes function broadly

- Alternatives to psuedcode:
	- Test-first development:
	- Refactoring:
	- Design-by-contract:
	- Hacking:


- Principle of proximity: Keep related code together

	- Keep references to variables close together
		- When code feels like it may be more appropriately declared elsewhere then at the top, then perhaps its time to make a new function
		- Keep things that operate on the same variable together

- hybrid coupling: When variables with specific values mean different things.
- Naming variables:
	- Describe what the variable represents 
	- Describes what it is generally, as opposed to in a computer sense
	- 10 to 16 characters long is ideal, 8-20 i fien though, etc. 
	- Longer names are better for rarely used/global variables, whilst shorter names are better for local/loop variables

	- Use consistent names for computed values.e.g Total/average/maximum/index/count/etc. etc.
		- Also ensure description is either a suffix/prefix butnot both
		- Try to make it clear and probably avoid using num
	- Use naming conventions for opposites for consistency. 		
	- There are several usual boolean names:
		- Done: For when task is done
		- Error: For when error has occured
		- Found: For when someting is found
		- Success/ok: For when task/operation is successful
		- Boolean names should imply true or false
		- Imagine if an 'is' is infront of the name to determine if it makes sense

	- Names consist of several things:
		- The contents of the variable
		- The kind of data
		- The scope of the variable

	- Ensure names can be pronounced

- Numbers in general:
	- Avoid magic numbers, other than for increments/decrements (i.e. 0, 1 are fine)
	- Anticipate divide-by-zero numbers
- Floating points:
	- Avoid adding numbers of different magnitudes, but if you have to sort the numbers before adding them etc., as this minimizes floating point errors
	- Avoid equality comparisons: Floating point numbers are not always equal. e.g. 0.1 added 10 times will not always equal 1.0
		- To fix this, determine a range of accuracy and return true if values are close enough and false otherwise

	- Changing floating point values to integers, where the decimal and the number part are integers can be used to maintain precision. Eg. cents range from 0-99. 
- Character/strings:
	- Avoid magic strings
	
- Boolean variables:
	- Use boolean variables to make expressions clearer. E.g. Instead of tons of ands, just use a variable
- Enumerated types:
	- Use it for readability (magic values may be replaced with enumerated types)
	- Enumerated types are a richer alternative to boolean variables
	

	- These next two require stylization and consideration
	- Define the first and last entries of an enumerated type for looping and size
		- E.g. Colour_size and colour_first for readability
	- Use the first entry to be an invalid type as it is often declared 0, e.g. use
	Colour_invalid = 0, then colour_first = 1, and so on

	- You can use enumerated types more than you expect for looping.
		- E.g. If looping across months, use an enumeration instead of i = 0 to 11 or something

- Named constants:
	- Use this to replce magic numbers
	- Always have a default in switch/else cases

- Arrays:
	-  It is always better to access arrays sequentially rather than randomly, so always consider container classes that you access sequentially- sets, stacks, queues etc. before considering an array
		- This results i less bugs

- Type aliasing:
	- Use it <- like a primitive type but where you can change representation
	- You can also create more specific types like array[1...NameLength] of char

	- Use names that correspond with real-world things rather than computer data. E.g. avoid BigInteger, because representationcs can change (functionally-oriented names)
	- Use your own type aliases as much as possible
	- Classes can be used as more complex types, when? (not sure when)




- Structures: These are data types built from other types (arrays are a special case)
	- There are several cases for using structures rather than classes:
		- Use structures to clarify data relationships
			- I.e. structures can be used to group related data
		- Use structures for operating on blocks of data:
			- I.e. When you need to swap data between two variables, you do it once instead of multiple times
		- Use structures to simplify parameter lists and when you are working with the whole data rather than individual entries:
			- Essentially group related structures (same as above)
			- Avoid passing the whole structure if only a few fields are needed
				- some information is hidden IN routines, and some is hidden FROM routines

		- Like normal types but for grouping related data such that it can be treated in bulk and individually, rather than just individually
			(-doesn't a class achieve this?)

		
- Pointers:
	- Just don't touch them if possible, rather abstract them away, maintain symmetry, always check them before use
	- Use a dog-tag <- this is where you add a field to a struct solely for error checkiiing, E.g. Put a value that should not change into the field <- if it has changed, then data has been corrupted
		- When freeing something, first set dog tag to invalid value before stopping
		- ALternative is to create two copies of fields (although this causes overhead)
		- Alternative is to overwrite deallocaed pointers with junk data/ set them to null
	- Allocate a memory parachute <- determine how much memory your program needs to save, cleanup and exit and reserve tht initally		
	- Just create a class for handling pointer operations and put all error handling in here to make sure it is consistent and safe
		- Just don't

- Global data:
	- Avoid it when possible 
	- There are several use cases:
		- Genuinly global data that needs to be used
		- For enums, cosntants and common data
		- For Tramp data: Data that is passed to a routine/class so it can be used by another routine or class

	- If you have to ensure, that accessing global data is done through methods for centralization, information hiding etc. 
		- i.e. Put data in a class and make it static, then write routines for accessing/manipulating data and use those eerywhere, to provide a level of abstraction
			- Ensure consistent abstraction level



- Statements:
	- Some statements are sequential, i.e. one statement must occur after another, it is important to make this as clear as possible:
		- Make dependences obvious including in routine names
			- If a routine name sounds bad, than this likely means the routine is bad
		- Make dependencies clear via returning and taking in values
		- Document unclear dependencies using comments
			- Generally document assumptions!!
		- Use assertions to force values to be initialiezed <- more complex but desirable in specific situations

	- Some statements don't care about order i.e. they can occur in any order:
		- In this case keep related actions together (law of proximtiy)


		- Make code read from top-to-bottom as opposed to jumping around
			- Keep code that manipulates the same data grouped together, rather than code that performs the same operations grouped together
				- The logic here is that we usually care about following a single piece of data rather than a set of operations
				- We can tell this is good because it reduces the span required to follow an object and also makes the code look like it can be broken into individual routines, rather than one big routine

			- Draw a box around code that is related - ideally this forms independent boxes

- Conditional statements:
	- Make the main path through code clear first and foremost 
		- Essentially put the main-case in the if rather than in the else
		- Especially important when dealing with nested if-else statements, this results in clearer code pathways
	- Remember the else clause:
		- Make sure you don't miss the else clause, as it is frequently missed when it shouldn't. This can include, using an else clause with null 
			- Make sure to add comments in this case

	- Chains of if-else can be simplified in several ways:
		- Use boolean functions for large conditions
		- Put the most common case first (i.e. case most likely to occur)
			- This is more performant and easier to debug
		- Use a default, 'else' case and use an assert if it shouldn't happen

		- Use cases instead

	- Case statements can be improved in several ways:
		- Use consistent ordering such as:
			- Most common cases
			- Normal cases
			- Alphabetical cases


		- Keep cases simple, <- move things into a routine if it gets to complex
		- Don't use phony variables for cases, i.e. sometimes it is better ot use multiple if/elses
		- Always use default case for handling 'default' only even if there is only one other case to handle
			- This also makes adding a new enum less annoying
			- default should be for error handling

		- Avoid fallthrough or if you do use it, make sure you have heavy documentation

		- Always use the most appropriate control flow


- While loops:
	- This should be used when you don't know how many times you will iterate
		- Tests at the beginning is standard
		- Tests at the end are equivalent to a do-while loop ( you use a while true loop at the start and break at the end)
		- Loop-with exits at the middle should be used whenever half the loop is outside the code (e.g. starting values for the loop) (you use a while true loop with a break at the middle)
		- Gotos could also be used but should be avoided
	- Put all the exit conidtions in one place

- For loops:
	- When you need code that executes a specific number of times (involving simple increments and decrements)
		- If there is any exit out of the loop then use a while loop
		- This is a simple loop
	- The loop statements should contain statements that initialize the loop, terminate it and/or moveit towards termination
	- Should use when there is only one exit condition (but avoid unless fixed/guaranteed exit position)

- For each loop:
	- This is useful for performing operations on each member of an array or container

- Loops in general:
	- Treat the inside of the loop as if it were a routine or black box
	- Only enter the loop from the top
	- Put initialization code directly before the loop
	- Avoid loops with empy body
	- Keep loop iterators/housekeeping at the end or beginning
	- Loops should follow single-responsibility principle and do only one  thing well, only combine for performance reasons after benchmarking
	- write code that doesn't depend on index's final value (i.e. keep it isolated)
	- Muliple breaks are likely a sign that a loop is doing too much and may be better off split into multiple loops
	- Use continues at the top of a loop, rather than anywhere else
		- If in the middle or end then use an if

	- Don't use breaks/continue if possible

	- Use ints not floats etc. for looping limits



	- Loops should be between 15-50 lines at most
		- The longer the loop the morelikely you should avoid breaks, continues etc.
	- Loops should be at most 3 levels
	- Loops should be able to be put in a routine

	- Loops can be simplified by creating inside-out:
		- Start by defining the inside of the loop without looping constructs then gradually define them as neccessary.
			- Repeat this process until you get the full loop

- For multiple returns:
	- Make sure that the returns follow the same 'purpose/responsibility'
	- Use guard clauses for error checking to avoid nesting

- Recursion:
	- Imaging the problem is solved already and imagine how to use that for the last case
	- Use that to create the current solution (which should be last solution)
	- Then add base case to the top


- Gotos are only useful in specific cases where they eliminate duplicate code
	- but they should always be avoided generally
	- They are used for having one location forcleaning up 
		- This can be replcaed with a loop and status variables
		- Or a try-finally loop can be used
		- There are essentially 3 approaches with trade-offs and it is up to you to decide
		- Just make it consistent

	- Just don't if possible but make sure that, gotos only go forward, all gotos are used 
		and gotos only reference things in one routine only. 

- Table driven methods: This uses tables instead of conditional statements and can do everything conditional statements
	- They are preferable when logic chains become more complex and they put knowledge into data rather than into logic
	- There are two issues with table driven methods:
		- First: How do you look up entries in the table
			- Direct vs indexed vs stair-step access
		- Second: What do you store in the table
			- You can store data, actions, references to routines etc.

	- Direct access: This is a simple look-up table that allows you to find the data you need directly
		- E.g Put days in month in a table as { 31, 28, 31, 30, etc..}\
			- As opposed to a function that returns everything
			- If you wanted to deal with leap years then convert it into a 2-dimensional array and let the secod index determine leap year or not
		- This can be extrapolated to more complex nested if statements, using enums for indexes in the table, thereby reducing it to a simple look-up
			- In this case you could also use switch expressions with tuples (??)
	

	- Flexible-Message-Format example:
		- In this situation the table specifies a format that encodes some behaviour and the program provides the elementary functions for that behaviour and uses it to get the desired results
			- E.g. Create a table of objects for desired functionality for ease as well
			- Look at book example
			- Important thing to realize: Neither functional/oop design resulted in a signficantly better design, rather a design based on a look-up table was better

	- Fudging look-up keys: Not all keys/values will index nicely into a table and this may require fudging in several ways:
		- Duplicate information 
		- Transform using a key to make it work directly by calling routine
			- A hash-map would achieve this equally effectively
		- In cases where  this is still not adequate an indexed-access table may be considered

- Indexed-access table:
	- The logic here is that an index-look-up table is provided that provides the index into the data table via the key, rather then going directly into the data table
		- This usually saves space compared to duplication
		- It also allows you to create a table that converts multiple keys into one, thereby avoiding complexity of a 3-dimensional table
		- It is more maintable and flexibible usually

- Stair-step access tables:
	- This is designed to represent complex ranges
	- The idea here is that you check relative to the upper end of each range and assign it a value
		- This works well with data at irregular intervals
		- it can be optimized with binary search
		- It has the advantage over other methods for working with decimals and such data


- Simplyfying boolean expressions:
	- break complicated tests into partial tests with new boolean variables/functions
		- This also gives the advantage that the name of the variable/function almost acs as documentation
	- Turn boolean tests into positives
		- This may be done more easily by usin de-morgans law, which allows you to simplify expressions
	- Put numeric expressions in number-line order, i.e. organize numeric tests so they follow the points on a number line. E.g. min_elements <= i and i <= max elements, as i is supposed to be in the middle this is more readable (makes it easy to visualize as lines)

- Guildlines for comparing 0:
	- Unless the result is a boolean, you should always explicitly compare it. This goes against c conventions but leads to more readability
	- E.g. 
		while (balance != 0) vs while (balance)
		or
		while(bufferPtr != null) vs while (bufferPtr) 

- Guidlines for empty conditionals
	- Make it clear via:
		- Using a comment or addin a method that does nothing doNothing() 
	- Avoid empty conditionals regardless

- Handling deep nesting (3-4 max):
	- Use retesting, where you test a case multiple times to split it apart (not always worth)
	- Use a break block (i.e. where you create a do while(false) loop for handling cases)
	- Use routines to extract out nesting
	- Use polymorphism and factory classes/normal classes to handle it

- structured porgramming: The core of this is that programs should use only one-in, onoe-out control constructs such that code can be read from top to bottom for the most part
- There are three components of structured programming:
	- Sequence: This is a set of statements executed in order
	- Selection: This is a control structure that causes satements to be executed selectively (i.e if-else)
	- Iteration: This is a control structure that causes statements to be executed multiple times
	- The core thesis of structured programming is that any control flow can be created from these three constructs. Hence break, continue, return, throw-catch etc. should be viewed with a critical eye

- Control flow is one of the major determinants of the complexity of a program
- THere are several ways of measuring control flow complexity:
	- Cyclomatic complexity metric: This is measured as the number of decision points in a routine, where each if/while/repeat/for/andor/case countds as 1 point for complexity
		- 0-5: probably fine
		- 6-10: start to think of simplifications
		- 10+: breka into a second routine
			- This doesn't reduce complexity, but rather the objects you need to juggle in your mind
	- Lines of code
	- Numer of nesting
	- Number of lines between successive reference
	- Number of lines that variable is in use
	- etc. 




- Personal rules:
	- Use brackets always (even for single if statements for defensive programming reasons)
	- The closer something represents a value or mathematical concept, like an angle or 3d point, the less likely it should be represented as an object but rather a type. If it is used primarily with operations then ideally it is closer to an expression style type (or object if that isn't possible).		
		- i.e. distinguish between objects that are more values that support composing, combining and expressiveness vs classes that support acccess control, specific functionnality etc. 
		- Why, I dunno?

	- Also just consider how likely to change
			- The closer somethnig is to a value or something that represents a mathematical concept, then it is likely to never change, in which case it should be a type

	- Consider ow frequently the data isused together (i.e. it should be disgustingly cohesive)

	- Types represent state/values, classes represent objects
		- 

	- Operations where order doesn't matter shold not be associated with an object, and should probably static (or better just a function)



	- Any rule that centralizes control oer things that might change is a good technique




- Treat every mapping as a database