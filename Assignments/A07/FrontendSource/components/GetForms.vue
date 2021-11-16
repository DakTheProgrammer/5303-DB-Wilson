<template>
  <div>
    <Button @pressed= "Click"/>
    <FormGetter :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import FormGetter from './FormGetter.vue'
import Button from './Button.vue'

export default {
  components:{
    FormGetter,
    Button,
  },
  data(){
    return{
      Api: "http://167.99.6.44:8004/forms",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    Click(){
      this.Send = this.Api
      this.Show++
    }
  }
}
</script>

<style>
#field
{
  color: black;
}
</style>
