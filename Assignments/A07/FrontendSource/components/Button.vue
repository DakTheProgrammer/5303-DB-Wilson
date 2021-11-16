<template>
  <div>
    <br>
    <button @click="Clicked()" type = 'button'>Submit</button>
  </div>
</template>

<script>

export default {
  data(){
    return{
      
    }
  },
  methods:
  {
    Clicked()
    {
      this.$emit('pressed')
    }
  }
}
</script>

<style>
button
{
  display:inline-block;
  padding:0.7em 1.4em;
  margin:0 0.3em 0.3em 0;
  border-radius:0.15em;
  box-sizing: border-box;
  text-decoration:none;
  font-family:'Roboto',sans-serif;
  text-transform:uppercase;
  font-weight:400;
  color:#eed4d4;
  background-color:#800000be;
  box-shadow:inset 0 -0.2em 0 -0.80em #747474;
  text-align:center;
  position:relative;
}
button:active
{
  top:0.1em;
}
@media all and (max-width:30em)
{
  button
  {
    display:block;
    margin:0.4em auto;
  }
}
</style>
