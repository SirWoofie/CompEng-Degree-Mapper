import random as rand
import json

# Global definitions
U = "Undergraduate"
G = "Graduate"
L = "Laboratory"
C = "Class Lecture Required"
D = "Discussion Required"

class course:
    
    def __init__(self, code: str = None, hours: int = None, name: str = "No name entered", career: list[str] = list[U], comp: list[str] = list[None], desc: str = None):
        self.code = code
        self.hours = hours
        # self.time = time # I would add this data, but it's almost impossible to obtain as a student. This project will assume the courses do not overlap or can be rescheduled instead.
        # self.days = days
        # self.length = length
        # self.semesters = semesters
        self.name = name
        self.career = career
        self.comp = comp
        self.desc = desc

    def print(self):
        return ("Code:" + self.code + " Hours:" + str(self.hours) + " Name:" + self.name + " Career:" + self.career[0] + " Components:" + self.comp[0] + " Description:" + self.desc)
    def printNoDesc(self):
        return ("Code:" + self.code + " Hours:" + str(self.hours) + " Name:" + self.name + " Career:" + self.career[0] + " Components:" + self.comp[0])
    def encode(self):
        return {"Code":self.code}


#Engineering Core Requirements (37 Semester Hours)
# TABLE 1. ENGINEERING CORE REQUIRED COURSES
CHM1045 = course("CHM 1045", 3, "General Chemistry I", [U], [C, D], "This course includes topics such as chemical symbols, formulas, and equations; states of matter; reactivity in aqueous solution; electronic structure, bonding, and molecular geometry. Students taking CHM 1045 after taking CHM 1020 and/or CHM 1032 may register for reduced credit, as indicated in the department's policy on reduced credit.") #This or BSC2020
BSC2010 = course("BSC 2010", 3, "Biological Science I", [U], [C], "This course is the first part of a two-semester introductory biology course designed for those interested in pursuing a career in life sciences. The course provides the building blocks necessary for a student to gain a strong foundation in general biology. Topics covered provide an overview of biological processes and function at the molecular, cellular and organismal level.") 

CHM1045L = course("CHM 1045L", 1, "General Chemistry I Laboratory", [U], [L], "This laboratory offers an introduction to quantitative techniques and to the chemical laboratory. Topics include stoichiometry, atomic spectra, thermodynamics, gases, as well as acids and bases, chemical structures, and reactivity.") #This or BSC2010L
BSC2010L = course("BSC 2010L", 1, "Biological Science I Laboratory", [U], [L], "This course introduces basic chemistry, energetics, metabolism, and cellular organization; molecular genetics and information flow; animal and plant function.")

PHY2048C = course("PHY 2048C", 5, "General Physics A", [U], [C], "This course is designed to provide students with an understanding of how and why things move. Topics covered include kinematics, forces, energy, momentum, oscillations, and thermodynamics. The course is intended for physical science majors and engineers and to be taken as a sequence with General Physics B (PHY 2049C) and Intermediate Modern Physics (PHY 3101). Completing Modern Physics entitles students to a minor in physics. Calculus is used in this course.") #This or PHY2048 and lab
# PHY2048 = course() # Course not offered
PHY2048L = course("PHY 2048L", 0, "General Physics Lab", [U], [L], "Course Description not on file") 

PHY2049C = course("PHY 2049C", 5, "General Physics B", [U], [C], "This course is a calculus-based introduction to electricity, magnetism, and optics for physical science majors. Course consists of lectures, recitations, and laboratory.") #This or PHY2049 and lab
PHY2049 = course("PHY 2049", 3, "General Physics B without Laboratory", [U], [D], "Same course as PHY 2049C, except that the student does not take the labora tory. May only be taken by students who have passed PHY 2054C or an equivalent course.")
PHY2049L = course("PHY 2049L", 0, "General Physics B Laboratory", [U], [L], "Course Description not on file")

MAC2311 = course("MAC 2311", 4, "Calculus with Analytic Geometry I", [U], [L], "This course covers polynomial, trigonometric, exponential, and logarithmic functions; first and second derivatives and their interpretations; definition and interpretation of the integral; differentiation rules; implicit differentiation; applications of the derivative; anti-derivatives; fundamental theorem of calculus. This course must be taken for reduced credit by students with prior credit for some of the content.")
MAC2312 = course("MAC 2312", 4, "Calculus with Analytic Geometry II", [U], [C], "This course covers techniques of integration; applications of integration; series and Taylor series; differential equations. This course must be taken for reduced credit by students with prior credit for some of the content.")
MAC2313 = course("MAC 2313", 5, "Calculus with Analytic Geometry III", [U], [C], "This course covers functions of several variables and their graphical representations; vectors; partial derivatives and gradients; optimization; multiple integration; polar, spherical, and cylindrical coordinate systems; curves; vector fields; line integrals; flux integrals; divergence theorem and Stokes' theorem. This course must be taken for reduced credit by students with prior credit for some of the content.")
MAP2302 = course("MAP 2302", 3, "Ordinary Differential Equations", [U], [C], "This course covers differential equations of the first order, linear equations of the second, systems of first order equations, power series solutions, Laplace transforms, numerical methods. Not open to students having credit in MAP 3305.")
MAS3105 = course("MAS 3105", 4, "Applied Linear Algebra I", [U], [C], "This course covers Gaussian elimination, vector spaces, least squares problems, determinants, eigenvalues and eigenvectors, linear transformations, applications.")

# TABLE II B. FLORIDA STATE UNIVERSITY STUDENTS
COP3330 = course("COP 3330", 3, "Data Structures, Algorithms and Generic Programming I", [U], [C], "This course focuses on object-oriented programming in a modern programming language; classes, objects, inheritance, and polymorphism; introduction to data structures and container classes.")
COP3353 = course("COP 3353", 1, "Introduction to UNIX", [U], [C], "This course for majors and non-majors offers an introduction to the UNIX operating system. Topics include: UNIX history, requesting UNIX accounts, logging into a UNIX system, basic operating system concepts and file structure, basic commands, text editor(s) (to include emacs, vi, and pico), printing, mail, and online help. The goals of this course are to enable students to log in to their UNIX accounts from any type of computer and to have a basic understanding of the commands and utilities.")
COP4530 = course("COP 4530", 3, "Data Structures, Algorithms, and Generic Programming", [U], [C], "This course focuses on definition, use, and implementation of generic data structures using a modern programming language; reusable program components. This course also provides introduction to analysis of the complexity of algorithms, including sorting and searching.")
MAD2104 = course("MAD 2104", 3, "Discrete Mathematics I", [U], [C], "This course covers techniques of definition and logical argument, sets and functions, propositional logic, introduction to graphs and relations, and  applications. Mathematics majors should take MGF 3301 instead of MAD 2104.")

# TABLE III. REQUIRED COMPUTER ENGINEERING COURSES (39 Semester Hours)
# Each student is required to complete 39 semester hours of required departmental courses. This includes 6 hours of required CpE laboratory. The courses shown in Table III are required CpE core courses.
EEL3002L = course("EEL 3002L", 2, "ECE Engineering Tools Lab", [U], [L], "This is an introductory laboratory for students entering the electrical and computer engineering programs. The basic topics include: lab safety issues; solving engineering problems using software tools such as MATLAB and Mathematica; electric circuit simulations using c software packages such as Multisim and OrCad; electric circuit design and instrumentation; the proper use of test and measurement equipment.")
EEL3003 = course("EEL 3003", 3, "Introduction to Electrical Engineering", [U], [C], "This course is an introduction to electrical engineering concepts for non-electrical engineering majors. The course focuses on circuit theory for interfacing sensors and actuators. Operational Amplifiers are included. Not accepted for credit towards BSEE.")
EEL3135 = course("EEL 3135", 3, "Signal and Linear System Analysis", [U], [C], "This course focuses on the classification and representation of signals and systems; Laplace transform; Z-transform; convolution; state variable techniques; stability and feedback.")
EEL3705 = course("EEL 3705", 3, "Digital Logic Design", [U], [C], "This course covers fundamental topics in digital logic design including the use of a hardware description language, as well as number systems, Boolean algebra, logic simplification, combinational and sequential logic circuits.")
EEL3705L = course("EEL 3705L", 1, "Digital Logic Laboratory", [U], [L], "This laboratory supports EEL 3705. This course introduces Electrical and Computer Engineering majors to various practical aspects of Digital Logic. This includes analysis, design and testing of digital logic circuits. Design and implementation are covered using Altera devices.")
EEL3927 = course("EEL 3927", 3, "Engineering Design Concepts", [U], [C], "This course introduces the skills and knowledge necessary to effectively complete a capstone project. Students are presented with concepts in design, systems engineering, project management, engineering team organization, ethics, and professionalism.")
EEL4021 = course("EEL 4021", 3, "Statistical Topics in Electrical Engineering", [U], [C], "This course examines the use of probability and statistical concepts in electrical engineering applications. Elementary probability-sets, sample spaces, axioms, joint and conditional probability. Random variables--distribution and density functions. Operations in random variables--expectation, moments, transformation of random variables. Introduction to random processes. Multiple random variables. Elements of statistics; parameter estimation and hypothesis testing.")
EEL4710 = course("EEL 4710", 3, "Introduction to Very High Speed Integrated Circuit Hardware Description Language", [U], [C], "This course offers an introduction to the VHDL hardware description language: data type, operations, combinational, sequential, components, functions, and procedures using VHDL. The course provides an overview of FPL devices and design tools. ")
EEL4710L = course("EEL 4710L", 1, "Introduction to VHDL Laboratory", [U], [L], "This laboratory course supports EEL 4710. The course introduces Electrical and Computer Engineering majors to various practical aspects of circuit design using Very High-Speed Integrated Circuits Hardware Description Language (VHDL).")
EEL4713 = course("EEL 4713", 3, "Computer Architecture", [U], [C], "This course presents modern computer architectures by studying how the relationships between hardware and software impact performance, machine language definition, processor data path and control designs, interfacing, and advanced topics.")
EEL4742 = course("EEL 4742", 3, "Advanced Microprocessor-Based System Design", [U], [C], "This course covers advanced concepts in microprocessor-based system design. Topics include microprocessor architectures, hardware/software synchronization, interrupts, interface protocols, power management, and introduction to real-time operating systems.")
EEL4742L = course("EEL 4742L", 1, "Advanced Microprocessor-Based System Design Laboratory", [U], [L], "This course is a laboratory in support of EEL 4742 Advanced Microprocessor-Based System Design. ")
EEL4746 = course("EEL 4746", 3, "Microprocessor-Based System Design", [U], [C], "This course explores fundamental concepts in microprocessor-based system design. Topics include: C and assembly level programming, computer architecture and organization, hardware timers, interrupt controllers, and device interfacing utilizing parallel and serial I/O.", )
EEL4746L = course("EEL 4746L", 3, "Microprocessor-Based System Design Laboratory", [U], [C], "Laboratory course in support of EEL 4746.")
EEL4911C = course("EEL 4911C", 3, "Senior Design Project I", [U], [C], "This course exposes senior students to concepts in design, project management, engineering team organization, and professionalism. Students are grouped into design teams where these principles are put into practice in organizing, proposing, and developing an engineering project. Periodic written reports and oral presentations and a final written proposal are required. The lecture material and texts provide instructions on project management, ethics, and design skills.")
EEL4914C = course("EEL 4914C", 3, "Computer Engineering Senior Design Project II", [U], [C], "This course exposes senior students to the concepts in design, project management, engineering team organization, ethics, design skills, and professionalism. Students are grouped into design teams where these principles are put into practice in organizing, proposing, and developing an engineering project. Periodic written reports and oral presentations, and a final written report are required.")

# TABLE IV. CORE COMPUTER ENGINEERING ELECTIVES (9 Semester Hours)
# All computer engineering majors are required to complete three of the following five CpE Core Electives (9 semester hours).
EEL4781 = course("EEL 4781", 3, "Computer Networks", [U], [C], "This course covers the fundamentals of computer network design and analysis; network architecture using a layered approach; analysis and examples of network protocols and standards; techniques for evaluating network performance selecting network protocols.")
EEL4759 = course("EEL 4759", 3, "Digital Image Processing", [U], [C], "This course is an introduction to image processing techniques, including theoretical development, analysis, and practical implementation. A project that includes implementation grounds the successful student in current engineering practice.")
EEL4347 = course("EEL 4347", 3, "Introduction to Cybersecurity", [U], [C], "This course is an introduction to computer security: symmetric ciphers, public-key cryptosystems, digital signatures, hashes, message authentication codes, key management and distribution, authentication protocols, vulnerabilities and malware, access control, network security.")
EEL4887 = course("EEL 4887", 3, "CpE Languages: Introduction to Python, Verilog, and MatLab/Simulink", [U], [C], "In this course, computer programming is used to improve quantitative problem-solving skills. This is a comprehensive course using the PYTHON, VERILOG and MATLAB/SIMULINK programming languages.")
EEL4873 = course("EEL 4873", 3, "Embedded Microprocessor System Design", [U], [C], "This course teaches students to be able to design, configure, and implement a complete embedded microprocessor system using soft-core, parameterized, or hard core microprocessors for FPGAs including required peripherals and software tools.")

# Computer Engineering Technical Electives (12 Semester Hours)
# Must complete 12 hours of technical electives. Six semester credit hours must be ECE technical electives.
EEL3111 = course("EEL 3111", 3, "Circuit Analysis I", [U], [C], "This course explores topics such as current, voltage, and power; resistors, inductors, and capacitors; network theorems and laws; operational amplifiers, phasors; impedances; sinusoidal steady-state analysis.")
EEL3112 = course("EEL 3112", 3, "Circuit Analysis II", [U], [C], "This course examines sinusoidal steady-state power analysis; three-phase circuits; operational amplifier; transient and forced response; frequency response; two-port networks; and circuit analysis.")
EEL3112L = course("EEL 3112L", 3, "Circuit Analysis II Lab", [U], [C], "This laboratory provides hands-on experience to electrical engineering majors in the fundamental topics of circuit analysis. It reinforces concepts introduced in the associated lecture.")

# Other technical electives
EEL4515 = course("EEL 4515", 3, "Digital Communication Systems", [U], [C], "This course covers topics such as sampling principle, spectral analysis of digital waveforms and noise, pulse and digital transmission systems, digital multiplexing, error probabilities, and system performance. ")

# Digital Literacy (0 hours beyond major) 
COP3014 = course("COP 3014", 3, "Programming I", [U], [C], "This course covers programming's fundamental concepts and skills in a high-level language that includes flow of control; data structures—arrays, strings, and structs; selection/iteration; procedural paradigm; interactive/file IO; and testing/debugging. Students evaluate and/or interpret digital data and/or their implications, and they demonstrate the ability to use digital technology effectively, correctly, and safely.") 
# Oral Communication Competency: (0 hours beyond major)
# Met by EEL4911C
# Scholarship in Practice: (0 hours beyond major) 
# Met by EEL4911C
# Formative Experience: (0 hours beyond major) 
# Met by EEL4914C
# Upper Division Writing: (0 hours beyond major)
# Met by EEL3927

# FSU Required Pre-requisite Courses (AA Courses?)
ENC1101 = course("ENC 1101", 3, "Freshman Composition and Rhetoric", [U], [D], "This course stresses the importance of critical reading, writing, and thinking skills, as well as the importance of using writing as a recursive process involving invention, drafting, collaboration, revision, rereading, and editing to clearly and effectively communicate ideas for specific purposes, occasions, and audiences. No auditors.")
ENC2135 = course("ENC 2135", 3, "Research, Genre, and Context", [U], [D], "This course emphasizes writing as a recursive process involving invention, drafting, collaboration, rereading, revision, and editing to compose in a variety of genres clearly and effectively for specific contexts, purposes, occasions, and audiences. The course teaches research skills that allow students to effectively incorporate outside sources in their writing.")
MAC1105 = course("MAC 1105", 3, "College Algebra", [U], [C, L], "This course is a review of algebraic operations, equations and inequalities; functions and functional notation; graphs; inverse functions; linear, quadratic, rational function; absolute value; radicals; exponential and logarithmic functions; system of equations and inequalities; applications. On the basis of test scores the student may be required to take a community college course before MAC 1105.")
MAC1147 = course("MAC 1147", 5, "Precalculus Algebra/Trigonometry", [U], [C], "This is a one-semester course encompassing the topics of MAC 1140 (Pre-calculus Algebra) and MAC 1114 (Analytic Trigonometry). See the topics for MAC 1140 and MAC 1114.")
MAT1033 = course("MAT 1033", 3, "Intermediate Algebra", [U], [C], "Course Description not on file")
MAC1140 = course("MAC 1140", 3, "Precalculus Algebra", [U], [C, L], "This course covers functions and graphs, especially high degree polynomial, rational, exponential, and logarithmic functions; systems of equations; solutions of linear systems; matrix methods; determinants; sequences and series; induction; and the binomial theorem. The course also explores applications, approximation, and methods of proof. May be taken concurrently with MAC 1114.")
EGN1004L = course("EGN 1004L", 1, "First Year Engineering Laboratory", [U], [L], "This course is intended to generate and maintain students' interest in the engineering disciplines so that they are motivated to become active learners, responsible students, and ethical engineering professionals.")

# List containing each entry in the hashmap. This can be used to iterate over the hashmap as otherwise the keys would be unknown.
entries = [CHM1045,
BSC2010,
CHM1045L,
BSC2010L,
PHY2048C,
PHY2048L,
PHY2049C,
# PHY2049,
PHY2049L,
MAC2311,
MAC2312,
MAC2313,
MAP2302,
MAS3105,
COP3330,
COP3353,
COP4530,
MAD2104,
EEL3002L,
EEL3003,
EEL3135,
EEL3705,
EEL3705L,
EEL3927,
EEL4021,
EEL4710,
EEL4710L,
EEL4713,
EEL4742,
EEL4742L,
EEL4746,
EEL4746L,
EEL4911C,
EEL4914C,
EEL4781,
EEL4759,
EEL4347,
EEL4887,
EEL4873,
EEL3111,
EEL3112,
EEL3112L,
EEL4515,
COP3014,
ENC1101,
ENC2135,
MAC1105,
MAC1147,
MAT1033,
MAC1140,
EGN1004L
]

# Dictionary to relate each entry in hashmap to a text string
maps = {}
maps = {CHM1045.code: CHM1045,
        BSC2010.code: BSC2010,    
        CHM1045L.code: CHM1045L,   
        BSC2010L.code: BSC2010L,   
        PHY2048C.code: PHY2048C,   
        PHY2048L.code: PHY2048L,   
        PHY2049C.code: PHY2049C,   
        # PHY2049.code: PHY2049,    
        PHY2049L.code: PHY2049L,   
        MAC2311.code: MAC2311,    
        MAC2312.code: MAC2312,    
        MAC2313.code: MAC2313,    
        MAP2302.code: MAP2302,    
        MAS3105.code: MAS3105,    
        COP3330.code: COP3330,    
        COP3353.code: COP3353,    
        COP4530.code: COP4530,    
        MAD2104.code: MAD2104,    
        EEL3002L.code: EEL3002L,   
        EEL3003.code: EEL3003,    
        EEL3135.code: EEL3135,    
        EEL3705.code: EEL3705,    
        EEL3705L.code: EEL3705L,   
        EEL3927.code: EEL3927,    
        EEL4021.code: EEL4021,    
        EEL4710.code: EEL4710,    
        EEL4710L.code: EEL4710L,   
        EEL4713.code: EEL4713,    
        EEL4742.code: EEL4742,    
        EEL4742L.code: EEL4742L,   
        EEL4746.code: EEL4746,    
        EEL4746L.code: EEL4746L,   
        EEL4911C.code: EEL4911C,   
        EEL4914C.code: EEL4914C,   
        EEL4781.code: EEL4781,    
        EEL4759.code: EEL4759,    
        EEL4347.code: EEL4347,    
        EEL4887.code: EEL4887,    
        EEL4873.code: EEL4873,    
        EEL3111.code: EEL3111,    
        EEL3112.code: EEL3112,    
        EEL3112L.code: EEL3112L,   
        EEL4515.code: EEL4515,    
        COP3014.code: COP3014,    
        ENC1101.code: ENC1101,    
        ENC2135.code: ENC2135,    
        MAC1105.code: MAC1105,    
        MAC1147.code: MAC1147,    
        MAT1033.code: MAT1033,    
        MAC1140.code: MAC1140,    
        EGN1004L.code: EGN1004L}

# "Course1" (key) requires (is adjacent to) ["Course2", "Course3", "Course4"] (elements in hashmap/dictionary)
a = {} # 'a' is the hashmap for course requirements
a[EEL3002L] = ([EEL3111, EEL3003],[])
a[EEL3003] = ([MAC2312, PHY2049],[])
a[EEL3111] = ([MAC2312],[PHY2049C])
a[EEL3112] = ([EEL3111, EEL3002L],[MAP2302])
a[EEL3112L] = ([EEL3111, EEL3002L],[EEL3112, MAP2302])
a[EEL3705] = ([],[COP3014, EEL3705L])
a[EEL3705L] = ([],[EEL3705])
a[EEL4021] = ([MAS3105, EEL3003],[]) #EEL3003 or EEL3112
a[EEL4347] = ([COP3014, EEL3705],[])
a[EEL4742] = ([EEL4746, EEL4746L],[EEL4742L])
a[EEL4742L] = ([EEL4746, EEL4746L],[EEL4742])
a[EEL4781] = ([COP3330],[])
a[EEL4911C] = ([EEL3135, EEL3927],[EEL4742]) #ACI: Oral Communication, Scholarship in Practice
a[EEL4887] = ([EEL4710],[COP3330])
a[EEL4914C] = ([EEL4911C],[]) #ACI: Formative Experience
a[EEL4710] = ([EEL3705, EEL3705L],[EEL4710L])
a[EEL4710L] = ([EEL3705, EEL3705L],[EEL4710])
a[EEL4713] = ([COP3014, EEL4746],[])
a[EEL4746] = ([COP3014, EEL3705, EEL3705L],[EEL4746L])
a[EEL4746L] = ([EEL3705, EEL3705L],[EEL4746])
a[EEL3135] = ([MAP2302, MAS3105],[EEL3003])
a[EEL3927] = ([ENC1101, ENC2135],[EEL4746])
a[EEL4759] = ([MAP2302],[])
a[EEL4873] = ([EEL3705],[])

# Other technical electives
a[EEL4515] = ([EEL3135],[EEL4021])

# Pre-engineering courses
a[CHM1045] = ([MAC1105],[]) #Higher or placement beyond MAC1105 is accepted
a[CHM1045L] = ([MAC1105],[CHM1045]) #Higher or placement beyond MAC1105 is accepted
a[BSC2010] = ([],[])
a[BSC2010L] = ([],[BSC2010])
a[PHY2048C] = ([MAC2311],[PHY2048L])
a[PHY2048L] = ([MAC2311],[PHY2048C]) # zero-credit-hour course.
# a[PHY2049] = ([PHY2048],[])
a[PHY2049C] = ([PHY2048C, PHY2048L, MAC2312],[PHY2049L])
a[PHY2049L] = ([PHY2048C, PHY2048L, MAC2312],[PHY2049C]) # zero-credit-hour course.
a[MAC2311] = ([MAC1147],[]) #MAC1147 OR [MAC1140, MAC1114] or suitable mathematics examination placement score.
a[MAC2312] = ([MAC2311],[])
a[MAC2313] = ([MAC2312],[])
a[MAP2302] = ([MAC2312],[]) #[MAC2312] or MAC2313 # Note: to take MAC2313, you need to have taken MAC2312 (or suitable mathematics examination placement score, which would simply give the credit for MAC2312). So I'll simplify and say MAC2312 is the requirement.
a[MAS3105] = ([MAC2312],[])
a[COP3330] = ([COP3014],[COP3353]) # COP3014 Or comparable course in C or C++ programming.
a[COP3353] = ([],[])
a[COP4530] = ([COP3330, MAD2104],[]) #Listed Coreq CDA3100 is not required for CpE students, only CS students.
a[MAD2104] = ([MAC2311],[]) #Or COP3014 and MAC1140. Reccomended prereq: [MAC2311]

# FSU Prerequisite courses
a[MAC1105] = ([MAT1033],[]) #Or suitable mathematics examination placement score. Recommended background: two years of high school algebra.
a[MAC1147] = ([MAC1105],[]) #Or suitable mathematics examination placement score.
a[ENC1101] = ([],[])
a[ENC2135] = ([ENC1101],[])
a[MAT1033] = ([],[])
a[COP3014] = ([MAC1140],[])
a[MAC1140] = ([MAC1105],[]) #Or MAC1114 or MAC2233 # Ignoring these two alternative options.
a[EGN1004L] = ([], [])

# Prerequisites are stored as the first item in the tuple accessed by a key in 'a'.
# Corequisites are stored as the second item in the tuple accessed by a key in 'a'.



# Testing entries
# EEL3002L.printNoDesc()
# for x in a[EEL3002L][0]:
#     x.printNoDesc()
# # Can the list be printed?
# print("\nPrint all adjacency lists with corresponding vertex")
# n = len(a)
# for v in range(0,n,):
#     print(v, "|", entries[v].name, ":", end = None)
#     print("Prerequisites: ", end = None)
#     for u in range(0, len(a[entries[v]][0])):
#         print(a[entries[v]][0][u].printNoDesc(), end = None)
#     print("Corequisites: ", end = None)
#     for u in range(0, len(a[entries[v]][1])):
#         if (a[entries[v]][1][u] != None):
#             print(a[entries[v]][1][u].printNoDesc(), end = None)
    
#     print()

# Store a sample semester-by-semester schedule
sample = []
sample.append([ENC1101, CHM1045, CHM1045L, MAC2311, EGN1004L, "GE Core Humanities/Cultural Practice"])
sample.append([ENC2135, MAC2312, PHY2048C, PHY2048L, COP3014, COP3353])
sample.append([MAD2104, "GE Ethics", "GE Core Social Science"])
sample.append([MAC2313, PHY2049C, PHY2049L, EEL3705, EEL3705L])
sample.append([MAS3105, MAP2302, EEL4746, EEL4746L, EEL3003, EEL3002L])
sample.append([COP3330, EEL3135, EEL4710, EEL4710L, EEL4742, EEL4742L])
sample.append([EEL4021, EEL3927, EEL4713, COP4530, "GE Ethics or Humanities"])
sample.append([EEL4911C, "Core Elective 1", "Core Elective 2", "Technical Elective 1", "Technical Elective 2"])
sample.append([EEL4914C, "Core Elective 3", "Technical Elective 1", "Technical Elective 2"])

# Now that entries have been validated, build a graph from them!

# Determine which courses have the most prerequisites
prereqs = []
totals = []
# for z in entries:
#     prereqs = a[z][0]
#     for x in prereqs:
#         for y in a[x][0]:
#             if (a[x][0][y] not in prereqs):
#                 prereqs.append(a[x][0][y])
#     totals.append(tuple(z), len(prereqs))
# print("Course totals: ", totals)

##############
# n = len(entries)
# for v in range(0,n): # Traverse a using entries as the indexer
#     prereqs = a[entries[v]][0]
#     # print("Prereqs", a[entries[v]][0])
#     for x in prereqs: # Traverse prereqs to ensure each is added.
#         for u in range(0, len(a[x][0])): # Traverse a selected course's list of prerequisites
#             # print("List:", a[x][0][u])
#             if (a[x][0][u] not in prereqs):
#                 prereqs.append(a[x][0][u])
#     totals.append((entries[v].code, len(prereqs)))

    
# Sort the totals
# totals.sort(key = lambda l: l[1])
# totals.reverse()
# print("Course totals:")
# for x in totals:
#     print(x)
    

# User interface section
# Ask user to input any courses taken, if they've met FSU requirements before admittance, etc.
# Ask user how many courses/hours they wish to take per semester
# Generate a list of reccomended courses on the map but display only one semester at a time.
# Allow multiple users/schedules to be planned

# print(maps)

class user:
    def __init__(self, name:str = "", startYear:int = None, startSemester:int = None, endYear:int = None, endSemester:int = None, taken:list[course] = list[None], semesters:list = list()):
        self.name = name
        self.taken = taken
        self.startYear = startYear
        self.startSemester = startSemester
        self.endYear = endYear
        self.endSemester = endSemester
        self.semesters = semesters

user1 = user("User1", 2024, 1, 2028, 1, [])


# Load data from file if user wants to
print("Do you wish to load data from a file? (y/n)")
doLoad = input()
(doLoad := True) if ( doLoad.lower()[0] == "y") else (doLoad := False)
if doLoad:
    print("Please enter the complete file name with extension: ")
    fileName = input()
    try:
        with open(fileName, 'r') as file:
            loadedCourses = json.load(file)
    except:
        print("Error loading file. Please restart program and try again.")
if doLoad:
    print(loadedCourses)
    count = 0
    loadSemester = []
    for sublist in loadedCourses:
        loadSemester = []
        for majig in sublist:
            name = list(majig.values())[0]
            
            loadSemester.append(maps[name])
            user1.taken.append(maps[name])
        count += 1
        user1.semesters.append(loadSemester)
    



# Input covered university requirements
# What level was earned from mathematics examination?
value = input("Is this the first semester being scheduled? (y/n)")
(value := True) if ( value.lower()[0] == "y") else (value := False)
mathTrue = False
math = None
validMath = {"MAC 1105": MAC1105,
                "MAC 1147": MAC1147,
                "MAT 1033": MAT1033,
                "MAC 1140": MAC1140,
                "MAC 2311": MAC2311,
                "MAC 2312": MAC2312,
                "MAC 2313": MAC2313
                }
if value:
    math = input("Based on the entrance mathematics examination score, what mathematics course should you start with? Enter in the format similar to \"XXX ####\"\n")
    if math in validMath:
        print("Credits accepted. First math course will be",validMath[math].code, "-", validMath[math].name)
        mathTrue = True
    elif ((math[0:2] + math[4:]) in validMath):
        print("Credits accepted. First math course will be",validMath[math[0:2] + math[4:]].code, "-", validMath[math[0:2] + math[4:]].name)
        mathTrue = True
    else:
        print("Invalid credits or credits not accepted")

def has_key(val):
    for key, value in a.items():
        if val == value:
            return True
    return False

# Input taken courses and earned credits
credits = []
# if mathTrue: credits.append(maps[math])
running2 = True
while (running2):
    running = True
    while(running):
        credit = input("Please enter any credits earned that are relevant to Computer Engineering. To finish, enter \"x\"")

        print("Entered:", credit)
        if (credit == "x"): running = False
        if (credit in maps): credits.append(maps[credit])

    for x in credits:
        print(x.code) 
    value = input("Are accepted credits correct? If so, enter \"y\". If a credit must be removed, enter \"r\"")
    (running2 := False) if ( value.lower()[0] == "y") else (running2 := True)
    (removing := True) if ( value.lower()[0] == "r") else (removing := False)
    if removing:
        credit = input("Please enter the course code of a credit to be removed from the taken list in the format \"XXX ####\"")
        if (credit in maps): credits.remove(maps[credit])

# Add credits to the user once the've been entered
for x in credits:
    if (x not in user1.taken):
        user1.taken.append(x)
print("\nCourses already taken by user:")
for x in user1.taken:
    print(x.code)



####################################################################################################################################################
########################################################## Start of main loop ######################################################################
####################################################################################################################################################
firstSemester = True
mainLoop = True
while mainLoop:
    # Determine what the highest math course taken is from the validMath list - if mathTrue then use that value instead as it's a first semester math course instead of based on previous credits.
    if mathTrue:
        highestMath = maps[math]
    else:
        highestMath = MAT1033 # Note: this is the lowest math course offered
        for x in user1.taken:
            if x.code in validMath:
                if (x.code[4:] > highestMath.code[4:]):
                    highestMath = x

    # Determine which courses can be taken now. This is based on courses already taken and courses planned to be taken for a semester before this planning.
    prereqs = []
    totals = []
    takenCourses = user1.taken
    availCourses = []

    n = len(entries)
    for v in range(0,n): # Traverse a using entries as the indexer
        prereqs = a[entries[v]][0]
            
        # Traverse the list of entries and use it to traverse the hashmap a.
        # For each entry, check if the list of takenCourses satisfies the prereqs for a course AND that this course is not in the takenCourses list. If so, add that course to the list of possible options.
        # print("Outer loop", entries[v].code)
        valid = True
        for x in prereqs: # Check the list of prereqs for a course.
            # print("In loop", x.code)
            if (("MAC" in x.code) or ("MAT" in x.code)) and (int(x.code[4:]) <  int(highestMath.code[4:])):
                # This math course prereq is already covered by the selected entrance math course
                # print("Skip prereq")
                continue
            if x not in user1.taken: # If any prereq viewed is not in takenCourses, then this course cannot be taken yet.
                valid = False

        if valid:
            availCourses.append(entries[v]) # If valid is still True after this, then, then add the course to the list!

    # Clean up any math courses already covered - typically just removes MAT 1033 as it has no prereqs to be checked.
    # print("Highest math:", highestMath.code)
    # Iterate through availCourses and remove any math courses that are below the already earned credit.
    for x in availCourses:
        if (x.code in validMath):
            if (x.code[4:] < highestMath.code[4:]):
                availCourses.remove(x)
                # print("Removed", x.code)

    if highestMath in availCourses:
        availCourses.remove(highestMath)

    # Display available courses, their names, and their corequisites. Coreqs are added automatically when a course is selected!
    print("\nAvailable courses:")
    for item in availCourses:
        valid = True
        # print("Math codes: ", item.code[4:], math[4:], mathTrue)
        # if ((item.code[-1] != "L") and (item.code[-1] != "C")):
        #     print("As int: ", int(item.code[4:]), int(math[4:]))
        # print("ITEM:", item.code)
        if (("MAC" in item.code) or ("MAT" in item.code)) and (int(item.code[4:]) <  int(highestMath.code[4:])):
                # This math course is already covered by the selected entrance math course, don't allow earlier math courses
                valid = False
                # print("Invalid because math code")
        if item in takenCourses:
            # print("Invalid takenCourses:", item.code)
            valid = False
        if valid:
            # Print coreqs if there are any
            if a[item][1]:
                print(item.code, ": ", item.name, " with Corequisites: ", sep = "", end = "")
                first = True
                for x in a[item][1]:
                    if first:
                        print(x.code, end = "")
                        first = False
                    else:
                        print(", ", x.code, end = "")
                else:
                    print()
            else:
            # Otherwise print without coreqs displayed
                print(item.code, ": ", item.name, sep = "")
            if (item.code == math):
                print("Note:", math, "is the math course to take next semester based on the entrance examination score. It is already added to the preferred courses list.")
    
    # Generate random selections of courses from the available courses. 12-18 hours, list how many. Allow user to select an option then continue to modifying it.
    print("\nGenerating sample semesters. Enter the minimum number of hours for generated semester. Recommended 12-18 hours. Classes are usually 3 hours while labs are 1 hour.")
    sampleHourLimit = input()
    valid = False
    while not valid:
        if sampleHourLimit.isnumeric:
            sampleHourLimit = int(sampleHourLimit)
            valid = True
        else:
            sampleHourLimit = input("Please enter a valid number.")
    sampleHourLimit = int(sampleHourLimit)

    # Initialize variables for use beyond loop
    randSemester = []
    randCourses = []
    running = True
    generating = True
    
    # Run any checks on course (can it be taken, coreqs, etc.)
    while generating:
        # Initialize variables
        
        randHours = 0
        randCoreqHours = 0
        sampleLengthList = []
        randSemester = []
        loopTimeout = 0
        exit = False
        # print("LOG: initialized i = ", i)
        # Add the first semester math course to the samples
        if (mathTrue and firstSemester):
            randSemester.append(maps[math])
            

        while not exit:
            # print("LOG: start of loop", n)
            if loopTimeout >= 50:
                print("LOG: Iterations limit reached.")
                exit = True
            if (randHours > sampleHourLimit):
                # If there are no hours remaining, exit loop
                print("LOG: no hours remaining, exiting")
                exit = True

            item : course = rand.choice(availCourses)
            # print("LOG: item is", item.code)

            randCoreqHours = 0
            # print("LOG: start of loop")
            if (("MAC" in item.code) or ("MAT" in item.code)) and (int(item.code[4:]) <  int(highestMath.code[4:])):
                # This math course is already covered by the selected entrance math course, don't allow earlier math courses
                # print("LOG: math invalid")
                loopTimeout += 1
                continue
            
            if ((item in takenCourses) or (item in randSemester) or (L in item.career)):
                # Course already taken, added, or a laboratory. Skip these.
                # print("LOG: in takenCourses")
                loopTimeout += 1
                continue
            
            for coreq in a[item][1]:
                randCoreqHours += coreq.hours # Add up all hours of all coreqs
                # print("LOG: coreq in a[item][1]")
            
            if (randCoreqHours + item.hours + randHours <= sampleHourLimit):
                # Do not add if it's too many hours.
                # print("LOG: hours > sampleHourLimit")
                randSemester.append(item) # Add item to randSemester
                randHours += item.hours
                loopTimeout = 0
                # print("LOG: appending", item.code)
                for coreq in a[item][1]: # For each coreq, add it to randCourses as well, but only if they're not already taken or added
                    if (coreq not in randSemester) and (coreq not in takenCourses):
                        # print("LOG: appending coreq:", coreq.code)
                        randSemester.append(coreq)
                        randHours += coreq.hours
            
            if (randHours > sampleHourLimit):
                # If there are no hours remaining, exit loop
                print("LOG: no hours remaining, exiting")
                exit = True

        del loopTimeout

        # Determine how many hours are in each sample semester
        print("\nGenerated sample semester", len(randCourses),":\n", sep = None)
        sampleLength = 0
        for thing in randSemester:
            sampleLength += thing.hours
        sampleLengthList.append(sampleLength)
        
        count = 0
        # Display the randomly generated list of courses.
        for thing in randSemester:
            print("Name:", thing.name, "Hours:", thing.hours)
            
        print("Total hours:", sampleLengthList[count], "Total courses:", len(randSemester))
        count += 1

        # Add the generated semester to the list of generated semesters.
        randCourses.append(randSemester)

        # Ask user if they wish to generate another semester
        print("Generate another sample semester? Enter \"y\".")
        value = input()
        if (value.lower()[0] != "y"): generating = False
            

    # Ask user to select a sample semester
    print("Please select a sample semester by entering the number associated with it. Alternatively, enter \"x\" to skip.")
    sampleSelected = False

    
    running = True
    while running:
        try:
            sampleSelection = input()
            if (value.lower()[0] == "x"): running = False
            sampleSelection = int(sampleSelection)
            print("Sample semester", sampleSelection, "selected.", sep = None)
            preferredCourses = randCourses[sampleSelection]
            sampleSelected = True
            running = False
        except:
            print("Error applying selected sample courses. Enter \"y\" to try again.")
            value = input()
            if (value.lower()[0] == "y"): running = False

    # print(randCourses[sampleSelection])

    # Ask user to select their preferred courses for next semester.
    print("Please select your courses for next semester. To finish, enter \"x\". To enter a course not listed in available courses, enter \"c\". To remove a course from this course list, enter \"r\". To fully reset the course list, enter \"reset\".")
    # Input taken courses and earned credits
    preferredCourses = []
    if sampleSelected:
        # print("LOG: Sample selected", sampleSelection)
        firstSemester = False
        for item in randCourses[sampleSelection]:
            preferredCourses.append(item)
    
    if (mathTrue and firstSemester and (maps[math] not in preferredCourses)):
        print("First-semester math course", math, "added.")
        preferredCourses.append(maps[math])
        firstSemester = False
    running2 = True
    while (running2):
        running = True
        credit = None
        while(running):
            credit = input()
            if ( credit.lower()[0] == "x"):
                credit = None
                break

            if ( (credit.lower()[0] == "c") and (len(credit) == 1)):
                # Special course that cannot be found in availCourses or maps
                credit = input("Please enter a course not found on the list of available courses. It will be added without any checks or course details, so use this feature sparingly!")
                hours = input("How many hours is this course?")
                specialCourse = course(credit, int(hours))
                print("Course added:", credit)
                preferredCourses.append(specialCourse)
            elif ("reset" in credit):
                doubleCheck = input("Are you sure? Enter \"reset\" again if you are certain you want to reset the course list for this semester.")
                if (doubleCheck == "reset"):
                    print("Resetting course list for this semester. After this, you may continue entering courses for this semester.")
                    preferredCourses.clear()
            elif ( credit.lower()[0] == "r"):
                value = input("Please enter the code for the course you wish to remove from this list. Please note, corequisites and prerequisites will not be checked in doing so.")
                if ((value in maps) and (maps[value] in preferredCourses)):
                    preferredCourses.remove(maps[value])
                    print("Removed", value)
                else:
                    # for item in preferredCourses:
                    #     if (item.code == value):
                    #         preferredCourses.remove(course(value))
                    print("Error removing course from list.")
            
            else:
                # Normal credit that can be found in availCourses
                if (maps[credit] in availCourses):
                    for x in a[maps[credit]][1]: # Add any corequisites if they aren't already taken
                        if (x not in user1.taken):
                            preferredCourses.append(x)
                            print("Coreq added:", x.code)
                    preferredCourses.append(maps[credit]) # Add selected course
                    print("Course added:", credit)
            
        print("Are entered courses correct? If so, enter \"y\"")
        totalHours = 0
        for x in preferredCourses:
            print(x.code, ", Hours: ", x.hours, sep = "")
            totalHours += x.hours
        
        if ((totalHours < 12) or (totalHours > 18)):
            #Too few or too many credit hours added to semester
            print("Warning: too few or too many credit hours added to schedule. Please adjust entered courses by first entering \"n\" then continuing with the prompt. You may ignore this warning by entering \"y\".")
        value = input()
        if ( value.lower()[0] == "y"):
            running2 = False
            break
        else:
            running2 = True

        print("Please select your courses for next semester. To finish, enter \"x\". To enter a course not listed in available courses, enter \"c\". To remove a course from this course list, enter \"r\". To fully reset the course list, enter \"reset\".")

    # Add preferred credits to the user once the've been entered - it's assumed that they'll be considered "taken" once entered.
    for x in preferredCourses:
        if (x not in user1.taken):
            user1.taken.append(x)

    # Debug: display list of currently taken courses
    value = input("\nView all taken courses? Enter \"y\" to view.")
    if (value.lower()[0] == "y"):
        print("Taken courses:")
        for x in user1.taken:
            print(x.code, ": ", x.name, sep = "")

    # Add the scheduled courses to the list of lists of semesters
    copyList = preferredCourses.copy()
    user1.semesters.append(list(preferredCourses))
    # Ask user if they wish to plan the following semester, assuming their current semester is completed successfully. If not, then exit the main loop, effectively ending the program.
    print("\nSchedule the another semester? If yes, enter \"y\".")
    value = input()
    if (value.lower()[0] == "y"):
        mainLoop = True
    else:
        mainLoop = False

####################################################################################################################################################
############################################################ End of main loop ######################################################################
####################################################################################################################################################

# Ask user to save contents to file
print("\nSave built semesters to file? (y/n)")
value = input()
(doSave := True) if ( value.lower()[0] == "y") else (doSave := False)
if doSave:
    print("Please enter a suitable filename without the extension: ")
    fileName = input()
    try:
        with open(fileName + ".json", 'w+') as file:
            json.dump(user1.semesters, file, indent=2, ensure_ascii=False, default=lambda o: o.encode())
    except:
        print("Error saving file. We are sorry for your loss of data.")


# Ask if user wishes to view all scheduled semesters?
print("\nView all scheduled semesters for this user? If yes, enter \"y\".")
value = input()
print()
if (value.lower()[0] == "y"):
    count = 1
    for x in user1.semesters:
        print("\nSemester ", count, ":", sep = "")
        for y in x:
            print(y.code, ": ", y.name, sep = "")
        count += 1

# Sort the totals
# totals.sort(key = lambda l: l[1])
# totals.reverse()
# print("Course totals:")
# for x in totals:
#     print(x)
####################################
if False:
    # How many years until planned graudation?
    endYear = int(input("Enter the year of planned graduation in the format \"####\": ")) # Assumption: 3 semesters per year (spring, summer, fall).
    running = True
    while(running):
        endSemester = str(input("Enter the semester of planned graduation (spring, summer, or fall): "))
        if endSemester.lower() == "spring":
            endSemester = 1
            running = False
        elif endSemester.lower() == "summer":
            endSemester = 2
            running = False
        elif endSemester.lower() == "fall":
            endSemester = 3
            running = False
        else:
            print("Error, invalid input.")
        
    startYear = int(input("Enter the year being planned for: "))
    startSemester = int(input("Enter the semester being planned for: "))
    running = True
    while(running):
        startSemester = str(input("Enter the semester of planned graduation (spring, summer, or fall): "))
        if startSemester.lower() == "spring":
            startSemester = 1
            running = False
        elif startSemester.lower() == "summer":
            startSemester = 2
            running = False
        elif startSemester.lower() == "fall":
            startSemester = 3
            running = False
        else:
            print("Error, invalid input.")

    totalSemesters = (endYear - startYear) + endSemester - startSemester

# # How many courses to take for next semester?
# num1, num2 = input ("Scheduling semester. How many courses do you want to take? Enter a minimum followed by a maximum. Example: \"# #\"").split()
# print("Entered:", num1, num2)
# # Typically, 3-5 courses per semester.



# # Begin traversing list of courses from the end. The final semester should have their senior design 2 course.
# endingCourses = []
# reqs = a[EEL4914C].first
# coreqs = a[EEL4914C].second
# numCourses = 1 + len(coreqs) # If a course is listed as a corequisite, it must be taken in the same semester.
# currentCourses = []
# scheduledSemesters.append(currentCourses)

# Mapping time
# Semester 1, Year 1
# CHM1045 + L or BSC2010 + L, Humanities/Ethics Statewide Core, ENC1101, MAC2311

# Check if prerequisites for these classes have been met.
# prereqs = a[CHM1045]
# missing = []
# if len(prereqs > 0):
#     for x in prereqs:
#         if x not in user1.taken:
#             missing.append(x)

# List all courses that the student can take (courses whose prereqs are satisfied). Give a suggested course list as well.
# Allow student/advisor to select their courses they can take for the upcoming semester.

# First, check which courses' prereqs are covered out of the master list.


print("\nEnd of program reached. Have a nice day!")