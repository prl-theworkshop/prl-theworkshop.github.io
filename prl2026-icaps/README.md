# PRL @ ICAPS 2026
[ICAPS'26](https://icaps26.icaps-conference.org)
<!-- todo: set link to PRL site of ICAPS when it is published -->
Dublin, Ireland \
Date: June 28 or 29, 2026 \
[prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com) \


## Aim and Scope

While *AI Planning* and *Reinforcement Learning* communities focus on similar
sequential decision-making problems, these communities remain somewhat unaware
of each other on specific problems, techniques, methodologies, and evaluations.

This workshop aims to encourage discussion and collaboration between researchers in the fields of AI planning and (reinforcement) learning. 
We aim to bridge the gap between the two communities, facilitate the discussion of differences and similarities in existing techniques, and encourage collaboration across the fields. 
We solicit interest from AI researchers that work in the
intersection of planning and (reinforcement) learning, in particular, those that focus on intelligent decision-making. This is the tenth edition of the [PRL workshop series](https://prl-theworkshop.github.io/) that started at [ICAPS 2020](https://icaps20subpages.icaps-conference.org/workshops/prl/).

PRL aims to coordinate with the workshops *Reliability In Planning and Learning* (RIPL) and *Language Models for Planning* (LM4Plan), with PRL covering the general intersection of learning and planning, RIPL covering the reliability-related aspects and LM4Plan covering the language model-related aspects of these areas. Joint sessions across workshops are a possibility that we will evaluate depending on submissions and workshop timing.

## Topics of Interest

We invite submissions at the intersection of AI Planning and (reinforcement) Learning. The topics of interest include, but are not limited to, the following

* Reinforcement learning (model-based, Bayesian, deep, hierarchical, etc.)
* Learning for planning (L4P)
* Generalized planning
* Monte Carlo planning
* Model representation
* Model learning
* Planning using approximated/uncertain (learned) models
* Learning search heuristics for planner guidance
* Theoretical aspects of planning and reinforcement learning
* Dataset and Benchmarks across planning and RL
* Action policy analysis or certification
* Reinforcement learning and planning competition(s)
* Multi-agent planning and learning
* Applications of both (reinforcement) learning and planning


## Important Dates

* Paper submission deadline: ~~May 10~~ ~~May 15~~ May 20 (final extension), AOE
* Paper acceptance notification: June 10, AOE

ICAPS will be **in-person** this year. Authors of accepted workshop papers are expected to physically attend the conference and present in person.

<!-- ## Schedule -->

<!-- 
# Program

## Keynotes 

### Marcus Hutter - Universal AI = General Planning + Reinforcement Learning

<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./marcus.jpg">
<h3><a target="blank" href="https://www.hutter1.net/">Marcus Hutter </a></h3>
 <h6> Senior Researcher, DeepMind and Professor, Australian National University</h6>
</div> 


##### Biography

Marcus Hutter is Senior Researcher at [Deep Mind]([http://www.deepmind.com/) and Professor in the [RSCS](http://cs.anu.edu.au/) at the [Australian National University](http://www.anu.edu.au).
He received his PhD and BSc in physics from the [LMU](http://www.en.uni-muenchen.de/) in Munich and a Habilitation, MSc, and BSc in informatics from the [TU Munich](http://www.in.tum.de/en.html).
Since 2000, his research at [IDSIA](http://www.idsia.ch/"), [ANU](http://www.anu.edu.au/), and [DeepMind](http://www.deepmind.com/) has centered around the information-theoretic foundations of      inductive reasoning and reinforcement learning, which has resulted in 200+ publications and several awards. His books on Universal Artificial Intelligence develop the first sound and complete theory of super-intelligent machines (ASI). He also runs the Human Knowledge Compression Contest (500'000€ H-prize).
     

#### Abstract
Classical Automated Planning considers deterministic, static, observable, known-world problems.
Classical Statistical Machine Learning primarily deals with i.i.d. classification, regression, and clustering.
Classical Reinforcement Learning aims at lifting many assumptions of both fields,
but makes its own assumptions such as on-policy learning in finite-state episodic/ergodic/stationary fully-observable MDPs.
Of course, all three fields have significantly broadened their reach to solve more general problems,
which naturally led to some convergence and increasing overlap. 
In this talk I will present, Universal Artificial Intelligence, a theory which unifies all three fields, lifting all assumptions mentioned above.
UAI well-defines optimal sequential decision-making in arbitrary unknown environments, which can serve as a gold-standard for more practical but limited approaches to aim at.

### Charles Gretton - How I Learned to Stop Worrying and Trust the ML

<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./charles-gretton.jpg">
<h3><a target="blank" href="https://comp.anu.edu.au/people/charles-gretton/">Charles Gretton </a></h3>
 <h6> Associate Professor, Australian National University</h6>
</div> 

#### Biography 

Charles Gretton is an Associate Professor in the School of Computing at the Australian National University (ANU) and the Director of Attention and Innovation for the Integrated AI Network. A researcher in Artificial Intelligence for over 20 years, he has contributed algorithms and analysis in the fields of automated planning, automated reasoning, and machine learning. His
research has been applied to a wide range of fields, including astronomy, mobile robotics, and large-scale business optimisation. In 2015, he co-founded the AI company HIVERY, at which he developed retail business optimisation solutions used in the USA, Japan, and Australia. He currently leads a research partnership with the Australian Institute of Health and Welfare, cybersecurity-related projects with Australian Commonwealth Government organisations, and is the Chief Scientific Investigator on a research agreement between ANU and the International Atomic Energy Agency. Released software tools associated with his recent research include: the HPC SAT/#SAT tool [Dagster](https://github.com/ANU-HPC/dagster), the related property directed reachability system [parallel-pdr](https://github.com/ANU-HPC/parallel-pdr), and the [state estimation tool for terrestrial instrumentation](https://github.com/GANs4AO/I2IT4AO).

#### Abstract

This talk presents a journey through research at the nexus of reinforcement learning and artificial intelligence planning. It explores the enduring challenge of creating general policies for sequential decision-making, particularly in problems with non-Markovian characteristics. We begin with foundational work in relational reinforcement learning that directly sought to bridge the gap between symbolic AI and statistical learning. This early research demonstrates how generalised policies can be learned over symbolic state representations, using techniques such as gradient-based policy optimisation and first-order logical regression to automate feature discovery.

The talk then pivots to contemporary challenges, where deep learning has become indispensable for reasoning under uncertainty in complex applications. This shift is illustrated through a case study in state estimation for terrestrial astronomy, where a deep neural network is trained to infer a latent, unobserved state of the world from sensor data. This technique has been employed as a state representation within a reinforcement learning agent. We then address the critical issue of model trustworthiness. We will present recent work on the formal verification of learned models, specifically using model checking techniques to prove properties of Physics-Informed Neural Networks (PINNs) that represent state with complex physical dynamics. There are compelling applications of planning to operation of complex systems, and the speaker argues the best approach is to build a full AI stack, starting with robust and performant state estimation.

## Talks 
Select accepted papers are given a slot in the program: 11 minutes for content + 4 minutes for questions.

## Poster Sessions
The program includes a poster sessions. All accepted papers must present a poster in the poster session.
<!--  -->


<!-- ## List of Accepted Papers  -->


## Submission Details


We solicit workshop paper submissions relevant to the above call of the following types:

 * Long papers -- up to 8 pages + unlimited references / appendices
 * Short papers -- up to 4 pages + unlimited references / appendices
 * Extended abstracts -- up to 2 pages + unlimited references/appendices 
 
Please format submissions in ICAPS style (see instructions in the [Author Kit](https://aaai.org/authorkit26-1/)). Authors submitting papers rejected from other conferences, please ensure you do your utmost to address the comments given by the reviewers. Please do not submit papers that are already accepted for the main ICAPS conference to the workshop. 
As this workshop is non-archival, you may submit already accepted papers from other conferences if they fit the workshop's scope. 

Some accepted long papers will be invited for contributed talks and potentially also a slot in the poster presentation session. 
<!-- ~~All accepted papers (long as well as short) and extended abstracts will be given a slot in the poster presentation session.~~  -->
All other accepted papers (long and short) and accepted extended abstracts will be given a slot in the poster presentation session. 
Extended abstracts are intended as brief summaries of already published papers,  preliminary work, position papers, or challenges that might help bridge the gap.

As the main purpose of this workshop is to solicit discussion, the authors are invited to use the appendix of their submissions for that purpose.


Paper submissions should be made through [OpenReview](https://openreview.net/group?id=icaps-conference.org/ICAPS/2026/Workshop/PRL).
<!-- Paper submission will be available soon.  -->

We do not insist on papers being submitted anonymously initially; this decision is left to the discretion of the author. If a paper is simultaneously being considered at a venue where anonymity is required, you have the option to submit it without author details, considering the possibility of a shared reviewer pool. However, please be aware that upon acceptance, the paper will be publicly posted on the PRL website with full author information.


## Organizing Committee
* [Zlatan Ajanović](https://zlatanajanovic.com), RWTH Aachen University, Aachen, Germany.
* [Dillon Ze Chen](https://dillonzchen.github.io), Laboratory for Analysis and Architecture of Systems (LAAS-CNRS), Toulouse, France.
* [Forest Agostinelli](https://cse.sc.edu/%7Eforesta/), University of South Carolina, Columbia, USA.
* [Timo P. Gros](https://mosi.uni-saarland.de/people/timo/), German Research Center for Artificial Intelligence (DFKI), Saarbrücken, Germany.
<!-- * [Sarah Keren](https://sarahk.cs.technion.ac.il), Technion, Israel Institute of Technology, Haifa, Israel. -->
* [Shahaf S. Shperberg](https://shperb.github.io), Ben-Gurion University, Be'er Sheva, Israel.
* [Ayal Taitler](https://sites.google.com/view/ataitler/home), Ben-Gurion University, Be'er Sheva, Israel.


Please send your inquiries to [prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com)

< [Link to other workshops in the series](https://prl-theworkshop.github.io)

