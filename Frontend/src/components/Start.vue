<template>
  <div class="content">
    <div class="box1">
       <a href="http://localhost:8080/#/login">
      <img alt="DB1" src="../assets/time.png" height = "200" width="320">
      <h1>DB MANMAN<br>Time Planner</h1>
      </a>
    </div>

    <div class="box2">
      <div class="Pad">
      </div>
      <div class="box21">
        <font size="2em" face="bold">ID : </font>
      </div>
      <div class="box22">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="box23">
        <input type="button" value="New Account" size=70 style = "width:80pt;height:16pt;text-align:center;">
      </div>
      <div class="Pad">
      </div>
    </div>

    <div class="box3">
      <div class="Pad">
      </div>
      <div class="box31">
        <font size="2em" face="bold">PW : </font>
      </div>
      <div class="box32">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="box33">
        <input type="button" value="Find PW" size=70 style = "width:80pt;height:16pt;text-align:center;">
        
      </div>
      <div class="Pad">
      </div>
    </div>

    <div class="box4">
      <div class="Pad">
      </div>
      <div class="box41">
        <input type="button" value="Log In" size=70 style = "width:100pt;height:18pt;text-align:center;">
      </div>
      <div class="box42">
        <input type="button" value="KAKAO Log In" size=70 style = "width:100pt;height:18pt;text-align:center;background-color:yellow;">
      </div>
      <div class="Pad">
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style>
.button {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}

a{text-decoration:none; color:black}

.content > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}

.content{
  display: grid;
  grid-template-rows: 400px 60px 60px 40px;
  grid-gap: 10px;
}
.Pad{
}

.box1{
}

.box2{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.box21{
}
.box22{
}
.box23{
}

.box3{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.box31{
}
.box32{
}
.box33{
}

.box4{
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}
.box41{
}
.box42{
}
.box43{
}
.box44{
}

#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>



