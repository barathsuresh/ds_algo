<h2><a href="https://leetcode.com/problems/encode-and-decode-strings">Encode and Decode Strings</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.</p>

<p>Machine 1 (sender) has the function:</p>

<pre>
string encode(vector&lt;string&gt; strs) {
  // ... your code
  return encoded_string;
}
</pre>

<p>Machine 2 (receiver) has the function:</p>
<pre>
vector&lt;string&gt; decode(string s) {
  //... your code
  return strs;
}
</pre>

<p>So Machine 1 does:</p>

<pre>
string encoded_string = encode(strs);
</pre>

<p>and Machine 2 does:</p>

<pre>
vector&lt;string&gt; strs2 = decode(encoded_string);
</pre>

<p><code>strs2</code> in Machine 2 should be the same as <code>strs</code> in Machine 1.</p>

<p>Implement the encode and decode methods.</p>

<p>&nbsp;</p>
<p><strong>Note:</strong></p>

<ul>
	<li>The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.</li>
	<li>Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.</li>
	<li>Do not rely on any library method such as <code>eval</code> or serialize methods. You should implement your own encode/decode algorithm.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Difficulty:</strong><br>
Medium</p>

<p><strong>Lock:</strong><br>
Prime</p>

<p><strong>Company:</strong><br>
Bloomberg Google Microsoft Square Twitter</p>
