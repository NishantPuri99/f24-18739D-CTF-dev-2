# CTF Challenge for 18-739D at CMU: Git-ting good at ret2win
<ol>
  <li>In this challenge, the player learns an important concept -> <i>git always remembers.</i></li>
<li>The player can netcat to a vulnerable C program server. The concept is simple -> Overflow the buffer and return to the win function.</li>
<li>The only issue is, there is no return address provided, neither is there an executable that the players can use.</li>
<li>The players are provided with a .git folder, however. By examining the z-lib compressed objects inside this directory, the user can extract the executable and learn some interesting git commands.</li>
<li>This challenge is inspired by this brilliant video by Rob Richardson <a href="https://www.youtube.com/watch?v=H5ZQuuygH7E">The definitive deep dive into the .git folder - Rob Richardson - NDC London 2024</a></li>
</ol>
