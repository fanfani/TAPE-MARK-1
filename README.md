# TAPE MARK 1

Python reconstruction of 1961 electronic poem "TAPE MARK 1" by Nanni Balestrini
*( currently on display at ZKM Karlsruhe: http://zkm.de/en/node/30507 )*


*REQUIREMENTS*: Python programming language, UNIX shell, C compiler


*HOWTO*: just loop the program in a UNIX terminal; for example, in a bash shell type

```while true; do ./tape_mark_1.py ; sleep 2 ; done```


*EYECANDY*: for adjusting the speed of typing you can compile slowcat.c and and pipe to it ;-)

```while true; do ./tape_mark_1.py | ./slowcat ; sleep 2 ; done```


“Tape Mark I” restoration project
----------------------------------

The “Tape Mark I” restoration project started in the fall of 2014 as part of a broader study on “prehistoric” software art. And of course, one of very first computer poems didn’t go unnoticed to our research. Furthermore, it was dated 1961 - a very early time of the computer age - and it was made by an italian writer we knew about and admired for his later work. Looking for more information about this historical event we got our hands on a copy of “Almanacco Letterario Bompiani 1962”, where the poem was first published alongside a detailed explanation of the program used to generate it. The first thing we did was to translate the simple generation rules described by Balestrini in a new software, written in a modern programming language (Python) and intended to be executed on contemporary computer systems.

Then, a weird idea came to our minds: to find the original media containing the software, run it again on the original hardware used in 1961 (an IBM mainframe) and document the whole thing. It came out that the Munich Science Museum has an IBM-7070 system in its permanent exhibit, and so we  decided to contact Nanni Balestrini and tell him about our idea. We met in Rome in April 2016 for an interview, edited as an upcoming video documentary by artist and filmmaker Federico Bonelli.

During our quest for the original “Tape Mark” program - still undergoing - we met Nanni for a second time and gave him the small wooden box you are looking at, as a present for his kindness. It hacks together our own Python program, a tiny “Raspberry Pi Zero” computer and an old portable TV set found at a flea market. 

**The MIAI and MusIF computer museums**

"Museo Interattivo di Archeologia Informatica" (MIAI) in Calabria and “Museo dell’Informatica Funzionante” (MusIF) in Sicily are two computer museums, both born in the early 00s and both located in southern Italy. After many years of collaboration the two institutions like to think of themselves as a single entity, geographically split in two complementary collections.

Our permanent exhibits of working historical computer systems are open to the public and can be visitable upon reservation. Visitors are welcome to interact with all the working machines experiencing the feel of old systems, softwares and interfaces. Combined, the two collections count thousands of vintage systems, ranging from early '60s computers to large mainframes, a timeline of home computers and videogame consoles, old Apple systems, IBM PC clones, UNIX workstations, and all kinds of weird peripherals. The exhibits include also a well stocked library, with more than 4000 documents among old books, technical manuals and magazines.

**Credits**

“Tape Mark I” restoration concept and software by Emiliano Russo - director of “Museo Interattivo di Archeologia Informatica”, Cosenza - web: http://verdebinario.org email: museo@verdebinario.org

Hardware concept and realization by Gabriele Zaverio - director of “Museo dell’Informatica Funzionante”, Palazzolo Acreide (SR) - web: http://museum.freaknet.org email: museum@freaknet.org

Wooden case design and realization by Vittorio Bellanich - Artist and artisan, Palazzolo Acreide (SR)
