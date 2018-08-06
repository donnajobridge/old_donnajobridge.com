Title: the eyes are the window to the brain
Slug: eyes
Date: 2018-07-25
Tags: memory, eye movements, cognitive neuroscience, data science
Image: /images/eye_icon.jpg

You’ve probably heard the eyes are the window to the soul, but I would say that the eyes are the window to the brain. The eyes provide so much information about what a person might be thinking or feeling, whether they are an expert or a novice, and even if they will later remember they’re currently viewing.

You might think that our eyes are mainly governed by perception -- something flashy catches our attention and we look there (think of a cat chasing around a laser pointer). Or, you detect some movement in the periphery, and you search around looking for the culprit (a spider, gahh!). Of course it is the case that perceptual shifts in the environment can guide our viewing behavior. But, our memory also plays a powerful role in what we look at. This has been a major focus of my research.

###background
Eye movements are at the cusp of unconscious vs. conscious processing in the brain. We move our eyes to distinct locations around 3-5 times per second. This rapid eye movement behavior can reveal real-time information about what we are thinking before we even have time to overtly verbalize it or make a voluntary response.

For instance, imagine seeing a friend after a few months. She looks like your same old friend -- but there is something different. You ask, have you lost weight? Did you get a tan? And then you finally realize, she has a new haircut! Even though it may have taken you a few moments to consciously realize the change in hairstyle, your eyes were probably quick to detect the difference. Without your knowledge you may have looked at her hair several times before you consciously realized that it was different. In fact, this behavior is probably what gave you that vague feeling that *something* had changed, even though you hadn’t quite put your finger on what it was. In this scenario, the memory of your old friend guided your eye movement to the changed feature (the haircut), and then your conscious awareness caught up.
<p align='center'>
![fig1](/images/haircut.png)
</p>
This simple example of detecting a difference about your friend highlights two key aspects of memory I’m most interested in: remembering familiar information and detecting new information. We are able to access existing memories and detect differences in the environment so rapidly that it feels like it occurs simultaneously. In fact, prior research has been unable to really pull apart these processes because we have lacked the tools to identify them in real time.

In a normal experiment, a subject is asked to determine if an image is identical to one they have seen before or if it has any differences. Subjects will look around for a few seconds and then make a single button press at the end of the trial. But as I mentioned in the [Consciousness Continuum](continuum.html) section, there are many steps involved that lead up to that final behavioral response. First you look around and scan the image. Detect any features that are familiar or distinct. Then, compare what you are looking at to your internal representation. Determine if there are any differences and then finally press a button indicating your response.

To really capture how our brain processes information in real time, I pioneered an approach using eye movements. I measured eye movements while recording brain activity from electrodes implanted deep into the brain of epilepsy patients, which allowed me to track memory processing as it unfolded rapidly over time. These patients have electrodes implanted deep into their brains temporarily so that doctors can monitor their seizures and identify the source of the epileptic activity. The electrodes were implanted into a structure, called the hippocampus, which is important for memory. It is difficult to measure activity directly from this area without these invasive electrodes, because it is located deep in the brain. As a researcher, I was able to gain access to these patients (and their brains) in the hospital when they had some free time between their busy clinical schedule.
<p align='center'>
<img src="/images/hpc_electrode.png" alt="hpc" style="width:50%;"/>
</p>

<!-- ![hpc](/images/hpc_electrode.png) -->
###research design
I designed a special memory task to differentiate remembering information from detecting new information using eye movements. In the memory task, I inferred that remembering information occurred when subjects looked at old content, whereas identifying new information occurred when subjects looked at new content. Using this technique, I was able to pull apart how these processes operate independently and interact on rapid time scales.
<video loop width="100%" autoplay>
  <source src="images/eyepath.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
In this task, subjects first studied objects in unique locations (see the apple on the left with eye movements superimposed). Later, subjects saw the same objects again, but this time, the objects appeared in updated locations. When this happened, subjects would detect the difference and look to the place where the object used to be on the screen (see the eye movements move from the apple's updated spot to its old spot on the screen).

The sequence of eye movements tended to occur in a specific order. Subjects would first view the object in its updated spot. During this time, they were likely identifying the object and remembering it from the earlier study phase. Then, they remembered the object's original location and look to that spot. After looking around the old spot, they would return their gaze to the object in its new spot. During this time, they could compare the location they are currently viewing to the location they have stored in their memory (see how the eyes move back and forth between the two spots).

####time course of fixations to the original and updated locations
<p align="center">
![fig2](/images/ls_kde_mismatch.png)
</p>
We next asked whether brain activity was linked to these eye movements, reflecting remembering the original location vs. detecting the new location. We looked at the raw electrical activity recorded from the hippocampus, which is located deep in the brain and important for memory. The raw electrical activity is composed of a mixture of different frequencies, which we can break down with a Fourier transform. When we apply the transform, we get distinct activity in the different frequency bands (from 3 to 100 Hz).

<p align='center'>
<img src="/images/eeg.png" alt="eeg" style="width:50%;"/>
</p>

After decomposing the raw electrical activity into separate frequency bands, the next step is to find significant effects. For this analysis, we compared brain activity across two different conditions. Here, we compared fixations to the original location versus fixations to the updated location. We obtained a series of difference values at each time-frequency point. We identify the individual time-frequency points that have large difference values. We then look for high scoring points that are contiguous on either the time or frequency scale. These contiguous points are called clusters. We then sum up the value of each unique cluster and assign a value to it.

![null](/images/null_distribution.png)

To distinguish significant effects from noise, we create a null distribution from the data. To do this, we shuffle the condition labels of each event and then re-run the comparison. We find the largest cluster from the random comparison and put that into the null distribution. We repeat this process 1000-10,000 times. Then, we see where the clusters from the real data fall in the null distribution.

###brain activity linked to eye movements
We found one cluster of activity that survived significance testing. This cluster was in a low frequency range called theta (3-8 Hz). Theta in the brain is important for forming memories. The idea is that this frequency range serves as a channel for the hippocampus to send information to other parts of the brain. Information sent on this channel allows the hippocampus memory system to direct behavior (e.g. tell the eyes where to look) and reinstate past experiences (e.g. visualize where the apple used to be).

![fig3](/images/hpc_phase.png)

The significant cluster of theta activity occurred in the hippocampus just before subjects looked to the object's old spot. This activity reflected the subject remembering where the apple used to be, and predicted that the subject was about to look to that spot. These findings show that our eye movements are precisely timed to thinking and behavior (this has never been shown before!). In this case, specific eye movements reflected remembering old experiences. These results provide concrete evidence that our eyes are powerful indicators of our thought processes.



###main points
* Eye movements are at the cusp of conscious vs. unconscious awareness
* Eye movements reveal what people are thinking and how the brain is processing information
* Designing specific tasks are required in order to harness the power of eye movements


###extrapolation
* Eye movements can be harnessed to gain insight into how people learn, what people like, what people pay attention to and what they later remember
* Eye movements provide a rich data set that can be combined with other measures (feedback, responses)
* Encountering interfaces, where do people expect a button or menu to be

#####citations
* [Bridge & Voss, 2015, Learning & Memory](/pdfs/bridge2015.pdf)
* [Bridge, Cohen, Voss, 2017, Journal of Cognitive Neuroscience](/pdfs/bridge2017.pdf)
* [Marin, VanHaerents, Voss, Bridge, 2018, eNeuro](/pdfs/marin2018.pdf)
* [Voss, Bridge, Cohen, Walker, 2017, Trends in Cognitive Neuroscience](/pdfs/voss2017.pdf)
