<h1> Red-black-tree</h1>
This is a dictionary which you can add and search its content using red black tree algorithm.

<p>
When you run the code it will display a menu which you can choose from to
<ol>
<li>Load</li>
<li>Print Dictionary Size</li>
<li>Insert word</li>
<li>Lookup a word</li>
<img src="assests/Screenshot (864).png"/>
</ol>
</p>
<p>
The dictionary name in the code is the same as the txt file uploaded in the repo, EN-US-Dictionary.

you can change it from the code
in this part:
<br/>
    def load(self, root):
    <br/>
        <h6>    hand = open("EN-US-Dictionary.txt", "r")</h6>


</p>
<p>
<h3>To load the dictionary:</h3>
<br/>
Enter 1
<img src="assests/Screenshot (865).png"/>

<h3>To check the size of the tree</h3>
<br/>
Enter 2
<img src="assests/Screenshot (866).png"/>

<h3>To insert a word</h3>
<br/>
Enter 3
<br/>
if the word isn't in the dictionary, it will display "Word (the word you entered) inserted successfully" and will display both the tree size and height
<br/>

However if the word is present in the dictionary, it will display "Word already in the dictionary"
<img src="assests/Screenshot (867).png"/>

<br/>

<h3>To search for a word</h3>
<br/>
Enter 4
<br/>
if the word is present in the dictionary, it will display "Yes,word in the dictionary"
<img src="assests/Screenshot (868).png"/>
<br/>
However if the word isn't in the dictionary, it will display "No,word isn't in the dictionary"
<img src="assests/Screenshot (869).png"/>

</p>