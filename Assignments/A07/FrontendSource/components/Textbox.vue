<template>
  <span id = "tb">
    <label>{{message}}:</label>
    <input @input="sendText()" v-bind:maxlength=maxLen v-model="text" type='text' size=35>
  </span>
</template>

<script>

export default {
  data(){
    return{
      text: ''
    }
  },
  methods:{
    sendText()
    {
      this.$emit('getText', this.text)
    }
  },
  props:{
    message: String,
    maxLen: Number
  }
}
</script>

<style>
input
{
  color: #747474;
  border-radius: 20px;
  border-color: #800000be;
  border-width: 3px;
}

label
{
  width: 125px;
  text-align: left;
  position: relative;
  bottom: 20px;
  left: 130px;
}

#tb
{
  position: relative;
  right: 50px;
}

</style>
