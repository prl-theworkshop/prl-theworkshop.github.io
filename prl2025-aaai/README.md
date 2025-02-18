# PRL @ AAAI 2025

[AAAI'25](https://aaai.org/conference/aaai/aaai-25/workshop-list/#ws34) \
Philadelphia, Pennsylvania, USA  \
Date: March 4, 2025, 8:30--6:00 \
Room: *120C*  \
[prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com)


> ❗Important Announcement
>
> Note that PRL will be a full day workshop starting at **8:30 AM** and ending at **6:00 PM**. 



## Aim and Scope

While AI Planning and Reinforcement Learning communities focus on similar
sequential decision-making problems, these communities remain somewhat unaware
of each other on specific problems, techniques, methodologies, and evaluations.

This workshop aims to encourage discussion and collaboration between researchers in the fields of AI planning and reinforcement learning. 
We aim to bridge the gap between the two communities, facilitate the discussion of differences and similarities in existing techniques, and encourage collaboration across the fields. 
We solicit interest from AI researchers that work in the
intersection of planning and reinforcement learning, in particular, those that focus on intelligent decision-making. This is the eigth edition of the [PRL workshop series](https://prl-theworkshop.github.io/) that started at [ICAPS 2020](https://icaps20subpages.icaps-conference.org/workshops/prl/).

## Program
The workshop location is *Room 120C* of the Pennsylvania Convention Center in Philadelphia, Pennsylvania.

## Schedule

| Time (Philadelphia) | Title |
|:------------:|:-----------|
|     8:30 - 10:30 am | **Session I** |
|         |  *Opening Remarks*   |
| | AI Planning: A Primer and Survey (Preliminary Report). <u>Dillon Ze Chen</u>, Pulkit Verma, Siddharth Srivastava, Michael Katz, and Sylvie Thiebaux. |
|         | **Keynote Anders Jonsson:<br>Exploiting Symbolic Structure and Hierarchy in Reinforcement Learning**    |
| | A Benchmark for Hierarchical Parameterized Action Markov Decision Process. <u>Dengxian Yang</u>, Neil Michael Dundon, Elizabeth J Rizor, Scott T. Grafton, Linda Ruth Petzold |
| | Contextual Bandits for Maximizing Stimulated Word-of-Mouth Rewards. <u>Ahmed Sayeed Faruk</u>, and Elena Zheleva. |
| | Planning with temporally-extended actions. <u>Palash Chatterjee</u>, and Roni Khardon.|
| 10:30 - 11:00 | Coffee break |
|  11:00 - 12:30 | **Poster Session** |
|  12:30 - 14:00 | Lunch |
|  14:00 - 15:30 | **Session II** |
|  | **Keynote Marlos Machado:<br>Representation-Driven Option Discovery in RL: Model-Free Success & Model-Based Challenges** |
|  | Active Teacher Selection for Reinforcement Learning from Human Feedback. <u>Rachel Freedman</u>, Justin Svegliato, Kyle Hollins Wray, and Stuart Russell. |
|  | HDDLGym: A Tool for Studying Multi-Agent Hierarchical Problems Defined in HDDL with OpenAI Gym. <u>Ngoc La</u>, and Ruaridh Mon-Williams |
|    15:30 - 16:00    | Coffee break    |
|    16:00 - 18:00   | **Session III** |
|  | **Keynote George Konidaris** |
|  | Overcoming Slow Decision Frequencies in Continuous Control: Model-Based Sequence Reinforcement Learning for Model-Free Control. <u>Devdhar Patel</u>, and Hava T Siegelmann.|
|  | Controller Synthesis from Deep Reinforcement Learning Policies. <u>Florent Delgrange</u>, Guy Avni, Anna Lukina, Christian Schilling, Ann Nowe, and Guillermo Perez. |
| | Intrinsic Self-Correction Enhancement in Monte Carlo Tree Search Boosted Reasoning via Iterative Preference Learning. Huchen Jiang, Yangyang Ma, CHAOFAN DING, Kexin Luan, and <u>XINHAN DI</u>. |
| | Exploring Explainable Multi-player MCTS-minimax Hybrids in Board Game Using Process Mining. <u>Yiyu Qian</u>, Tim Miller, and Liyuan Zhao. |
| | *Closing Remarks* |


##  Keynotes

### Exploiting Symbolic Structure and Hierarchy in Reinforcement Learning

<div style="text-align: center;">
<img style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./anders.png">
<h3><a target="blank" href="https://www.upf.edu/web/anders-jonsson">Anders Jonsson</a></h3>
 <h6>Full Professor, Universitat Pompeu Fabra</h6>
</div> 

#### Abstract
A well-known limitation of reinforcement learning is its high sample complexity, which causes learning to be slow in complex tasks. The situation is even worse in problems with non-Markovian dynamics, i.e. when the ability to predict the future depends on the entire interaction history. In this talk I will describe two recent lines of work that improve the sample complexity of reinforcement learning by exploiting the symbolic structure of tasks. The first line of work is to train a set of policies for solving subtasks in an existing hierarchy, and combine these policies for fast or zero-shot learning of more complex, global tasks. The second line of work is to learn finite-state automata for non-Markovian decision processes, providing symbolic information that compactly captures the interaction history.

### Representation-Driven Option Discovery in RL: Model-Free Success & Model-Based Challenges

<div style="text-align: center;">
<img  style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="./marlos.png">
 <h3><a target="blank" href="https://webdocs.cs.ualberta.ca/~machado/">Marlos Machado</a></h3>
 <h6>Assistant Professor, University of Alberta</h6>
</div> 

#### Abstract
The ability to reason at multiple levels of temporal abstraction is a fundamental aspect of intelligence. In reinforcement learning, this attribute is often modelled through temporally extended courses of action called options. Despite their popularity as a research topic, options are rarely a core component of traditional RL solutions. In this talk, I will introduce a general framework for option discovery that leverages the agent’s representation to identify useful options. By using these options to generate a rich stream of experience, the agent can improve its representations and learn more effectively in model-free settings across diverse environments with varying topologies and observation spaces. However, options are far less common–and often less effective–in planning. I will also present insights into making options more useful for planning and the challenges posed by function approximation in this setting.

### Signal to Symbol  (via Skills)

<div style="text-align: center;">
<img  style="border-radius: 50%;overflow: hidden;background-color:#373737;height: 200px;object-fit: cover;" width="200px"  src="gdk-photo3.jpg">
<h3><a target="blank"  href="https://cs.brown.edu/people/gdk/">George Konidaris</a></h3>
<h6>Associate Professor, Brown University</h6>
</div> 

#### Abstract

I will address the question of how an RL agent with a rich
sensorimotor space can learn abstract, task-specific representations of
a particular task, and the conditions under which such representations
match classical planning paradigms. I will tale a constructivist
approach, where the computation the representation is required to
support - here, planning using a given set of motor skills - is
precisely defined, and then its properties are used to build the
representation so that it is capable of doing so by construction. The
result is a formal link between the skills available to a robot and the
symbols it should use to plan with them. I will present an example of a
robot autonomously learning a (sound and complete) abstract
representation directly from sensorimotor data, and then using it to
plan. I will also argue that this re-representation step is a critical
component of solving the general AI problem.




## Accepted Papers

#### Oral Only

* [Exploring Explainable Multi-player MCTS-minimax Hybrids in Board Game Using Process Mining](papers/2.pdf), *Yiyu Qian, Tim Miller, Liyuan Zhao* 
* [HDDLGym: A Tool for Studying Multi-Agent Hierarchical Problems Defined in HDDL with OpenAI Gym](papers/5.pdf), *Ngoc La, Ruaridh Mon-Williams*
* [Planning with temporally-extended actions](papers/8.pdf), *Palash Chatterjee, Roni Khardon*
* Contextual bandits for maximizing stimulated word-of-mouth rewards, *AHMED SAYEED FARUK, Elena Zheleva*
* [Active Teacher Selection for Reinforcement Learning from Human Feedback](papers/12.pdf), *Rachel Freedman, Justin Svegliato, Kyle Hollins Wray, Stuart Russell*
* [AI Planning: A Primer and Survey (Preliminary Report)](papers/14.pdf), *Dillon Ze Chen, Pulkit Verma, Siddharth Srivastava, Michael Katz, Sylvie Thiebaux*
* [Intrinsic Self-Correction Enhancement in Monte Carlo Tree Search Boosted Reasoning via Iterative Preference Learning](papers/17.pdf), *Huchen Jiang, Yangyang Ma, CHAOFAN DING, Kexin Luan, XINHAN DI*
* [A Benchmark for Hierarchical Parameterized Action Markov Decision Process](papers/19.pdf), *Dengxian Yang, Neil Michael Dundon, Elizabeth J Rizor, Scott T. Grafton, Linda Ruth Petzold*
* [Overcoming Slow Decision Frequencies in Continuous Control: Model-Based Sequence Reinforcement Learning for Model-Free Control](papers/22.pdf), *Devdhar Patel, Hava T Siegelmann*
* [Controller Synthesis from Deep Reinforcement Learning Policies](papers/23.pdf), *Florent Delgrange, Guy Avni, Anna Lukina, Christian Schilling, Ann Nowe, Guillermo Perez*
  
#### Poster Only

* [Concurrent Learning with Aggregated States via Randomized Least Squares Value Iteration](papers/3.pdf), *Yan Chen, Qinxun Bai, Shi Dong, Maria Dimakopoulou, Yiteng Zhang, Zhengyuan Zhou* 
* [Liner Shipping Network Design with Reinforcement Learning](papers/4.pdf), *Utsav Dutta, Yifan Lin, Zhaoyang Larry Jin*
* [ContextFormer: Stitching via Expert Calibration](papers/7.pdf), *Ziqi Zhang, Jingzehua Xu, Jinxin Liu, Zifeng Zhuang, Donglin Wang, Miao Liu, Shuai Zhang*
* [RELAX: Reinforcement Learning Enabled 2D-LiDAR based Autonomous System for Parsimonious UAVs](papers/9.pdf), *Guanlin Wu, Zhuokai Zhao, Huan Chen, Jinyi Zhao, Yangke Zhang, Yutao He*
* [InterLevel: Synthesizing Stair-Navigation Skills in Character-Scene Interactions](papers/10.pdf), *Jack Shilton, Boeun Kim, Hyung Jin Chang*
* [Neurosymbolic Reinforcement Learning With Sequential Guarantees](papers/13.pdf), *Lennert De Smet, Gabriele Venturato, Luc De Raedt, Giuseppe Marra*
* [SPRIG: Stackelberg Perception-Reinforcement Learning with Internal Game Dynamics](papers/15.pdf), *Fernando Martinez, Juntao Chen, Yingdong Lu*
* [Gen-HypRL : Generative Policy learning Framework for Multi-Task Reinforcement Learning](papers/20.pdf), *Jayaram Reddy, Sanket Hemant Kalwar, Brojeshwar Bhowmick, Arun Kumar Singh, Madhava Krishna*
* [Networked Restless Multi-Arm Bandits with Reinforcement Learnin](papers/24.pdf), *Hanmo Zhang, Kai Wang*
* [Average-Reward Reinforcement Learning with Entropy Regularizatio](papers/26.pdf), *Jacob Adamczyk, Volodymyr Makarenko, Stas Tiomkin, Rahul V Kulkarni*

  
<!-- 
## Topics of Interest

We invite submissions at the intersection of AI Planning and Reinforcement Learning. The topics of interest include, but are not limited to, the following

* Model-Based, Hierarchical and Safe Reinforcement Learning
* Monte Carlo planning
* Model representation and learning for planning
* Planning using approximated/uncertain (learned) models
* Learning to Search
* Theoretical aspects of planning and RL
* Action policy analysis or certification
* RL and Planning competition(s), datasets, and benchmarks
* Multi-agent planning and learning
* Applications combining RL and Planning
* Integration of planning and RL for hierarchical approaches
* Integrating Planning and RL for exploration (Planning-based exploration in RL)
* Combining RL and Planning for interpretability and explanations


## Important Dates


> ❗Important Announcement
>
> Deadlines have changed and we have added abstract submission deadline.
>
> Given the timeline, we welcome papers under review at the AAAI main conference. We request the authors to inform us if the paper is accepted at AAAI, when the decisions are out.


* Abstract submission deadline: ~~Sunday, December 1st, 2024~~ 
* Paper submission deadline: ~~Sunday, December 8th, 2024~~  *(extended)*
* Paper acceptance notification:  ~~Monday, December 16th, 2024~~  *(extended)*

All deadlines are AoE

Submission site: [OpenReview](https://openreview.net/group?id=AAAI.org/2025/Workshop/PRL)

AAAI will be **in-person** this year. Authors of accepted workshop papers are expected to physically attend the conference and present in person.
--> 
<!-- 

## Schedule

TBA

# Program

tba


## Keynotes 

 ## List of Accepted Papers

--> 
<!-- 
## Submission Details


We solicit workshop paper submissions relevant to the above call of the following types:

 * Long papers -- up to 8 pages + unlimited references / appendices
 * Short papers -- up to 4 pages + unlimited references / appendices
 * Extended abstracts -- up to 2 pages + unlimited references/appendices 
 

Papers must be formatted in AAAI two-column; see the [AAAI-25 author kit for details](https://aaai.org/authorkit25/).  Authors submitting papers rejected from other conferences, please ensure you do your utmost to address the comments given by the reviewers. ~~Please do not submit papers that are already accepted for the main AAAI conference to the workshop.~~ Given the timeline, we welcome papers under review at the AAAI main conference. We request the authors to inform us if the paper is accepted at AAAI, when the decisions are out.

Some accepted long papers will be invited for contributed talks. All other accepted papers (long and short) and accepted extended abstracts will be given a slot in the poster presentation session.  Extended abstracts are intended as brief summaries of already published papers,  preliminary work, position papers, or challenges that might help bridge the gap.

As the main purpose of this workshop is to solicit discussion, the authors are
invited to use the appendix of their submissions for that purpose.


Paper submissions should be made through [OpenReview](https://openreview.net/group?id=AAAI.org/2025/Workshop/PRL).

We do not insist on papers being submitted anonymously initially; this decision is left to the discretion of the author. If a paper is simultaneously being considered at a venue where anonymity is required, you have the option to submit it without author details, considering the possibility of a shared reviewer pool. However, please be aware that upon acceptance, the paper will be publicly posted on the PRL website with full author information.

-->


## Organizing Committee

* [Zlatan Ajanović](https://zlatanajanovic.com), RWTH Aachen, Aachen, Germany
* [Timo P. Gros](https://mosi.uni-saarland.de/people/timo/), German Research Center for Artificial Intelligence (DFKI), Saarbrücken, Germany
* [Floris den Hengst](https://florisdh.nl), University of Amsterdam, Amsterdam, Netherlands
* [Daniel Höller](https://fai.cs.uni-saarland.de/hoeller/), Saarland University, Saarbrücken, Germany
* [Harsha Kokel](http://harshakokel.com), IBM Research, San Jose, USA
* [Ayal Taitler](https://sites.google.com/view/ataitler/home), Ben-Gurion University, Be'er Sheva, Israel


Please send your inquiries to [prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com)

<br/>
<br/>
<br/>
<br/>

< [Link to other workshops in the series](https://prl-theworkshop.github.io)

