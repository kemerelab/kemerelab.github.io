tite:Differences in Spatial Coding during Slow and Fast Gamma
slug:gamma-bands-and-theta-sequences
---
Welcome to the first recap of our lab's journal club! This week we covered [Zheng et al.'s Spatial Sequence Coding Differs during Slow and Fast Gamma Rhythms in the Hippocampus](http://www.cell.com/neuron/abstract/S0896-6273(15)01076-4). 

The sequential firing of place cells as an animal traverses its place fields is a well-documented phenomenon. One way to analyze place cell activity is to look at the spikes relative to the theta oscillation (~6-10 Hz), which are known as [theta sequences](http://onlinelibrary.wiley.com/doi/10.1002/hipo.20345). Likewise, aligning the spikes to the gamma oscillation (~25-100 Hz) results in gamma sequences. The authors specifically investigated theta sequences relative to slow (~25-55 Hz) and fast (~60-100 Hz) gamma ("theta-nested gamma sequences"). 

This image is a nice summary of the hypotheses the paper examined:
![](/content/images/2016/10/pic-1.jpg)
The hypotheses concerned the path length/trajectories encoded within a gamma sequence. In hypothesis A, **discrete spatial locations** are encoded within an individual gamma cycle. Thus, the trajectories encoded during fast gamma will span a greater distance than those during slow gamma because there are more fast gamma cycles within one theta cycle. On the other hand, hypothesis B claims that a **sequence** of locations is represented within an individual slow gamma cycle. Then, a theta-nested gamma sequence will cover greater distance during slow gamma than during fast gamma.

The authors found that slow gamma sequences had significantly larger temporal compression (locations spanned by the sequence aka "x-span" divided by the duration of the sequence aka "t-span") than fast gamma sequences. Bayesian analysis was used to decode the sequences and showed that the locations represented during fast gamma correlated much better with current location of the animal than did slow gamma, which had higher temporal compression. The t-spans of slow and fast gamma sequences were not significantly different, countering the argument that slow gamma could have spanned a longer distance merely because the sequence duration was greater. As usual, it helps to have a figure. Note that the dotted white line represents the animal's current location.
![](/content/images/2016/10/pic-2.jpg)

One of the most important results was the presence of phase precession in gamma sequences. In a theta sequence, a place cell will fire at an earlier and earlier phase of an individual theta cycle as an animal moves through that cell's place field. Thus, the phase of a spike reveals information about where in the place field the animal is. Phase procession was observed for slow gamma but not fast gamma sequences, suggesting that the phase of slow gamma codes spatial information. 

Finally, the authors found that the number of fast gamma cycles per theta cycle increased with path length of the theta sequence. The number of slow gamma cycles did not increase likewise. Assuming hypothesis B, the result for fast gamma is consistent. That is, if a discrete spatial location is encoded within an individual fast gamma cycle, to span a longer path in one theta cycle, there would need to be more fast gamma cycles. In the case of slow gamma, it is less clear whether the results support hypothesis B. For example, if we know that place cells A,B,C fire in a slow gamma sequence and that the number of gamma cycles per theta cycle does not increase, in order to span a longer path, more than 3 place cells would fire within the same number of gamma cycles, such as place cells A,B,C,D,E. This doesn't necessarily imply that the basic unit of a slow gamma cycle is a sequence of locations rather than discrete locations, as hypothesis B proposes.

While the results did not provide conclusive support for hypothesis B, the paper nonetheless gave a plausible working model, linking fast gamma to encoding of current location in real time and slow gamma to retrieval of stored memories in a time-compressed fashion. We look forward to future studies about the characterization and functionality of different gamma rhythm subtypes!




