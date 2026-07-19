# PRL @ ICAPS 2026
[ICAPS'26](https://icaps26.icaps-conference.org)
<!-- todo: set link to PRL site of ICAPS when it is published -->
Dublin, Ireland \
Date: June 28 \
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
## Schedule

| Time (Dublin) | Title |
|:------------:|:-----------|
| 9:00 |**Opening Remarks** |
| 09:05 - 10:35 | **Session I**|
|              | Kristina Levina, Nikolaos Pappas, Athanasios Karapantelakis, Aneta Vulgarakis Feljan, Jendrik Seipp - Reinforcement Learning for Long-Horizon Unordered Tasks: From Boolean to Coupled Reward Machines |
|              | Andy Edmondson, Ron Petrick - PBRMS: Priority-Based Reward-Machine Switching for Context-Aware Reinforcement Learning in Non-Stationary POMDPs |
|  | Jonas Reiter, Jakob Elias Gebler, Hector Geffner - Differentiable Learning of Lifted Action Schemas for Classical Planning |
|  | Yuval Aroosh, Ayal Taitler - Model-Driven Policy Optimization in Differentiable Simulators via Stochastic Exploration |
|  | Magnus Cunow, Nicola J. Müller, Timo P. Gros, Gregor Behnke, Daniel Höller - An Admissible Neuro-Symbolic Landmark Cut Heuristic – Preliminary Results |
|  | Jonas Gösgens, Niklas Jansen, Hector Geffner - Learning Lifted Action Models from Traces with Minimal Information About Actions and States |
| 10:35 - 11:05 | *Coffee Break*    |
| 11:05 - 12:00 | **Keynote Alfonso Emilio Gerevini and Ivan Serina:<br>On Learning Planning Heuristics and General Policies through GNNs and Transformers**    |
| 12:00 - 13:00 | **Session II** |
|  | Markus Fritzsche, Elliot Gestrin, Jendrik Seipp - Symmetry-Aware Transformer Training for Automated Planning |
|  | Gustavo De Mari Pereira, Leliane N. de Barros - Effective Reinforcement Learning Exploration in Stochastic Shortest Paths with Dead-Ends |
| | S.T. Lin - On the Possibility of Solving STRIPS Planning Problems with REINFORCE |
| | S.T. Lin, Nicola J. Müller, Tim Nico Bauerschmidt, Chaahat Jain, Jörg Hoffmann, Isabel Valera - Using a Search-Based Safety Oracle for RL Policy Fine-Tuning |
|  14:30  - 15:25 pm  | *Lunch Break*   |
| 14:30 - 15:25 am| **Keynote Joerg Hoffmann and Chaahat Jain:<br>Automatic Safety Debugging of Tree-Ensemble Action Policies in AI Planning**   |
| 15:25 am - 16:00 pm | **Session III** |
|  | Srinivas Nedunuri, Douglas Cale Crowder - Synthesis of Shields for Safe Reinforcement Learning in Both Discrete and Continuous State and Action Spaces |
|  | Arman Mohammadi, Markus Fritzsche, Jendrik Seipp - Towards Symbolic Planning via Diffusion |
|  | Forest Agostinelli - The DeepXube Software Package for Solving Pathfinding Problems with Learned Heuristic Functions and Search |
| 16:00 - 16:30 pm | *Coffee Break*    |
| 16:30  - 17:30 pm | **Session IV**    |
| | Arnaud Lequen, Clément Legrand-Lixon, Léo Saulières - Pareto Q-Learning with Reward Machines |
| | Yusuf Syed, Viraj Parimi, Brian C. Williams - MoMo: Conditioned Contrastive Representation Learning for Preference-Modulated Planning |
| | Forest Agostinelli, Shahaf S. Shperberg - Data Efficient Training of Heuristic Functions for Satisficing Search |
| | Misagh Soltani, Forest Agostinelli - Heuristic Learning and Search Without Exhaustive Action Enumeration |
| 17:30 pm | **Closing Remarks** |

# Program

## Keynotes 

### Alfonso Emilio Gerevini and Ivan Serina - On Learning Planning Heuristics and General Policies through GNNs and Transformers

<div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap;">
<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./AlfonsoGerevini.jpeg">
<h3>Alfonso Emilio Gerevini</h3>
<h6>Full Professor, University of Brescia, Italy</h6>
</div>
<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./assoc-prof-dr-ivan-serina.jpg">
<h3>Ivan Serina</h3>
<h6>Associate Professor, University of Brescia, Italy</h6>
</div>
</div>

#### Abstract

Recent advances in deep learning have opened new opportunities for automated planning, while also raising fundamental questions about how learned models can acquire, represent, and exploit planning knowledge. In this talk, we will discuss recent work on learning-based approaches to planning, with a focus on the interaction between neural models and symbolic planning systems.
The talk will cover methods for learning heuristic functions in lifted classic and numeric planning through Graph Neural Networks, where planning states are encoded as relational structures enriched with propositional and numeric information used to guide search. It will also present transformer-based approaches for learning general planning policies, with particular emphasis on PlanGPT models trained from planning instances to generate action sequences for new problems in the same domain.
A central theme of the talk will be the synergistic integration of neural learning from data and model-based planning. Learned components can capture reusable knowledge, guide search, or suggest candidate plans, while symbolic models and validators remain essential for enforcing action semantics and validating generated plans to preserve correctness. We will also discuss connections with reinforcement learning as well as the challenges of generalization, robustness, and integration of neural components into planning systems.

#### Biography

**Alfonso Emilio Gerevini** is Professor of Computer Science at the University of Brescia, Italy, where he leads a research group in AI planning and machine learning. He has received eight awards from the International Conference on Automated Planning and Scheduling (ICAPS), including two Influential Paper Awards in 2019 and 2023 (honourable mention), and five awards from the International Planning Competitions.
Over more than thirty years of research in AI planning, he has worked on a wide range of topics. His most recent work focuses on resilient/robust planning, linear temporal logics for planning, and neural and neuro-symbolic learning for general planning policies, search heuristics, and goal recognition.
He is a Fellow of the European Association for Artificial Intelligence (EurAI), the International Academy of Artificial Intelligence Sciences (AAIS), and the International Artificial Intelligence Industry Alliance, and a member of the European Laboratory for Learning and Intelligent Systems (ELLIS). He has served the AI and planning communities in various roles, including as Program Co-Chair of ICAPS 2009, Conference Co-Chair of ICAPS 2026, and Associate Editor of the Artificial Intelligence Journal.

**Ivan Serina** is Associate Professor at the Department of Information Engineering of the University of Brescia, Italy. His research focuses on automated planning, heuristic search, plan generation and adaptation, case-based planning, and the integration of machine learning and deep learning techniques into planning systems. He has been a member of the Artificial Intelligence Research Group at the University of Brescia since 1997 and has contributed to the development of planning systems such as LPG. His recent work investigates neural approaches to planning, including Graph Neural Networks for learning planning heuristics and transformer-based models for learning general planning policies, as well as applications of AI planning and optimization techniques to water management.

### Joerg Hoffmann and Chaahat Jain - Automatic Safety Debugging of Tree-Ensemble Action Policies in AI Planning

<!-- <div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./joerg_hoffmann.jpg">
<h3>Joerg Hoffmann</h3>
<h6>Full Professor, Saarland University, Saarbrücken, Germany</h6>
</div> -->

<div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap;">
<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./joerg_hoffmann.jpg">
<h3>Joerg Hoffmann</h3>
<h6>Full Professor, Saarland University, Saarbrücken, Germany</h6>
</div>
<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  
src="./chaahat1.jpg">
<h3>Chaahat Jain</h3>
<h6>PhD Student, Saarland University, Saarbrücken, Germany</h6>
</div>
</div>


#### Abstract

Safety is a key concern for learned action policies. Here we discuss a complete methodology toolbox allowing to effectively find unsafe policy runs, find the action decisions causing unsafety on these runs, repair the policy to fix these decisions, and verify that the repaired policy is safe. Together, these tools form a fully automatic safety debugging loop for learned policies. We realize this loop in numeric planning under initial-state and action-outcome uncertainty, with the policy objective being to reach the goal while avoiding unsafe states. We focus on tree ensembles as the policy representation, as in our setting these imitate neural teacher policies.

#### Biography

**Joerg Hoffmann** is a Professor of CS at Saarland University, Saarbrücken, Germany. He has published more than 200 scientific papers, has been Program Co-Chair of AAAI'12 as well as Conference Co-Chair of ICAPS 2010 and 2020, and has received various prizes including the EurAI Dissertation award 2002. His core research area is AI automated planning, with connections to related fields such as ML and verification, and a recent focus on quality assurance for learned action policies. He is a Fellow of AAAI and EurAI.

**Chaahat Jain** is a PhD student at the chair of Prof. Jörg Hoffmann in the CS
department at Saarland University, Saarbrücken, Germany and a member of
the Neuroexplicit Models of Language, Vision and Action research
training group. His research lies in the learning, safety verification,
and repair of action policies in planning. Specifically, he is focused on
understanding how possible policy representations, from symbolic
formulations to machine learning models such as neural networks, effects
their quality and reparability.

<!-- 
# Program (placeholder from prior year)

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
## Accepted Papers
* [talk] [Reinforcement Learning for Long-Horizon Unordered Tasks: From Boolean to Coupled Reward Machines](papers/2_Reinforcement_Learning_for_L.pdf) ([OpenReview](https://openreview.net/forum?id=AfRCCaEXq2)), *Kristina Levina, Nikolaos Pappas, Athanasios Karapantelakis, Aneta Vulgarakis Feljan, Jendrik Seipp*
* [talk] [PBRMS: Priority-Based Reward-Machine Switching for Context-Aware Reinforcement Learning in Non-Stationary POMDPs](papers/3_PBRMS_Priority_Based_Reward_.pdf) ([OpenReview](https://openreview.net/forum?id=L8h7f4sk6l)), *Andy Edmondson, Ron Petrick*
* [talk] [Differentiable Learning of Lifted Action Schemas for Classical Planning](papers/4_Differentiable_Learning_of_L.pdf) ([OpenReview](https://openreview.net/forum?id=fjPZgmKg1b)), *Jonas Reiter, Jakob Elias Gebler, Hector Geffner*
* [talk] [MoMo: Conditioned Contrastive Representation Learning for Preference-Modulated Planning](papers/5_MoMo_Conditioned_Contrastive.pdf) ([OpenReview](https://openreview.net/forum?id=QME33nC8aB)), *Yusuf Syed, Viraj Parimi, Brian C. Williams*
* [talk] [An Admissible Neuro-Symbolic Landmark Cut Heuristic – Preliminary Results](papers/6_An_Admissible_Neuro_Symbolic.pdf) ([OpenReview](https://openreview.net/forum?id=nQak2eOgt2)), *Magnus Cunow, Nicola J. Müller, Timo P. Gros, Gregor Behnke, Daniel Höller*
* [talk] [Model-Driven Policy Optimization in Differentiable Simulators via Stochastic Exploration](papers/7_Model_Driven_Policy_Optimiza.pdf) ([OpenReview](https://openreview.net/forum?id=O57GJQNfi2)), *Yuval Aroosh, Ayal Taitler*
* [talk] [Learning Lifted Action Models from Traces with Minimal Information About Actions and States](papers/9_Learning_Lifted_Action_Model.pdf) ([OpenReview](https://openreview.net/forum?id=gdnBpd1ntg)), *Jonas Gösgens, Niklas Jansen, Hector Geffner*
* [talk] [Symmetry-Aware Transformer Training for Automated Planning](papers/10_Symmetry_Aware_Transformer_.pdf) ([OpenReview](https://openreview.net/forum?id=9Gx5s2sc6d)), *Markus Fritzsche, Elliot Gestrin, Jendrik Seipp*
* [talk] [Effective Reinforcement Learning Exploration in Stochastic Shortest Paths with Dead-Ends](papers/11_Effective_Reinforcement_Lea.pdf) ([OpenReview](https://openreview.net/forum?id=YyFb5zQ5PY)), *Gustavo De Mari Pereira, Leliane N. de Barros*
* [talk] [Synthesis of Shields for Safe Reinforcement Learning in Both Discrete and Continuous State and Action Spaces](papers/13_Synthesis_of_Shields_for_Sa.pdf) ([OpenReview](https://openreview.net/forum?id=kp7kIujk3F)), *Srinivas Nedunuri, Douglas Cale Crowder*
* [talk] [Towards Symbolic Planning via Diffusion](papers/14_Towards_Symbolic_Planning_v.pdf) ([OpenReview](https://openreview.net/forum?id=wNfICOZzWU)), *Arman Mohammadi, Markus Fritzsche, Jendrik Seipp*
* [talk] [On the Possibility of Solving STRIPS Planning Problems with REINFORCE](papers/15_On_the_Possibility_of_Solvi.pdf) ([OpenReview](https://openreview.net/forum?id=QroQkGBJYU)), *S.T. Lin*
* [talk] [Using a Search-Based Safety Oracle for RL Policy Fine-Tuning](papers/16_Using_a_Search_Based_Safety.pdf) ([OpenReview](https://openreview.net/forum?id=eG4u8O10a5)), *S.T. Lin, Nicola J. Müller, Tim Nico Bauerschmidt, Chaahat Jain, Jörg Hoffmann, Isabel Valera*
* [talk] [Pareto Q-Learning with Reward Machines](papers/17_Pareto_Q_Learning_with_Rewa.pdf) ([OpenReview](https://openreview.net/forum?id=0LmlpddShf)), *Arnaud Lequen, Clément Legrand-Lixon, Léo Saulières*
* [talk] [Data Efficient Training of Heuristic Functions for Satisficing Search](papers/19_Data_Efficient_Training_of_.pdf) ([OpenReview](https://openreview.net/forum?id=dviGgWaoHj)), *Forest Agostinelli, Shahaf S. Shperberg*
* [talk] [Heuristic Learning and Search Without Exhaustive Action Enumeration](papers/21_Heuristic_Learning_and_Sear.pdf) ([OpenReview](https://openreview.net/forum?id=H4CpM0PP8w)), *Misagh Soltani, Forest Agostinelli*
* [talk] [The DeepXube Software Package for Solving Pathfinding Problems with Learned Heuristic Functions and Search](papers/18_The_DeepXube_Software_Packa.pdf) ([OpenReview](https://openreview.net/forum?id=CDaiA6keWn)), *Forest Agostinelli*

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
* [Zlatan Ajanović](https://zlatanajanovic.com), UAS Technikum Wien, Vienna, Austria.
* [Forest Agostinelli](https://cse.sc.edu/%7Eforesta/), University of South Carolina, Columbia, USA.
* [Timo P. Gros](https://mosi.uni-saarland.de/people/timo/), German Research Center for Artificial Intelligence (DFKI), Saarbrücken, Germany.
* [Shahaf S. Shperberg](https://shperb.github.io), Ben-Gurion University, Be'er Sheva, Israel.
* [Ayal Taitler](https://sites.google.com/view/ataitler/home), Ben-Gurion University, Be'er Sheva, Israel.


Please send your inquiries to [prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com)

< [Link to other workshops in the series](https://prl-theworkshop.github.io)

