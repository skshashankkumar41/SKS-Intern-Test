<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="SKSInternTest_0"></a>SKS-Intern-Test</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Exercise_1_2"></a>Exercise 1</h2>
<ul>
<li class="has-line-data" data-line-start="3" data-line-end="17">
<p class="has-line-data" data-line-start="3" data-line-end="4"><strong>Files and Usage</strong></p>
<p class="has-line-data" data-line-start="5" data-line-end="6"><strong><a href="http://getFaceValue.py">getFaceValue.py</a></strong> - A function getFaceValue that takes string as parameter and return its extracted facevalue,</p>
<pre><code class="has-line-data" data-line-start="8" data-line-end="10"> python exercise-1/getFaceValue.py --text &quot;Your Text With Facevalue&quot;
</code></pre>
<p class="has-line-data" data-line-start="11" data-line-end="12"><strong><a href="http://checkPerformance.py">checkPerformance.py</a></strong> - It has 3 functions to calculate performance of faceValue extraction based on dollor signs, “save/off” keywords etc. It will print all 3 perfomance metrics.</p>
<pre><code class="has-line-data" data-line-start="14" data-line-end="16"> python exercise-1/checkPerformance.py 
</code></pre>
</li>
</ul>
<h2 class="code-line" data-line-start=17 data-line-end=18 ><a id="Exercise_2_17"></a>Exercise 2</h2>
<ul>
<li class="has-line-data" data-line-start="18" data-line-end="37">
<p class="has-line-data" data-line-start="18" data-line-end="19"><strong>Files and Usage</strong></p>
<p class="has-line-data" data-line-start="20" data-line-end="21"><strong><a href="http://ner-data-creator.py">ner-data-creator.py</a></strong> - It creates data in the format required by spacy by extracting nouns from the coupons corpus [will be entity] and after doing some preprocessing.</p>
<pre><code class="has-line-data" data-line-start="22" data-line-end="24"> python exercise-2/ner_data_creator.py 
</code></pre>
<p class="has-line-data" data-line-start="24" data-line-end="25"><strong><a href="http://train-ner.py">train-ner.py</a></strong>- It trains the ner data created by <a href="http://ner-data-creator.py">ner-data-creator.py</a> using spacy and saves the ner model in the same directory.</p>
<pre><code class="has-line-data" data-line-start="26" data-line-end="28"> python exercise-2/train_ner.py 
</code></pre>
<p class="has-line-data" data-line-start="28" data-line-end="29"><strong><a href="http://get-entity.py">get-entity.py</a></strong> - It takes a string as arguement and returns the dictonary with keys as entity type and value as entity</p>
<pre><code class="has-line-data" data-line-start="30" data-line-end="32"> python exercise-2/getEntity.py --text &quot;Text containing Entities&quot; 
</code></pre>
<p class="has-line-data" data-line-start="32" data-line-end="33"><strong><a href="http://entityOnAllData.py">entityOnAllData.py</a></strong> - It just creates the dataframe showing actual and predicted entities on our created ner dataset</p>
<pre><code class="has-line-data" data-line-start="34" data-line-end="36"> python exercise-2/entityOnAllData.py 
</code></pre>
</li>
</ul>