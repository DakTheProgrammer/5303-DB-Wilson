<template>
  <div>
    <Textbox message="M#" :maxLen="12" @getText = "ChangeMnu"/>
    <Button @pressed= "Click"/>
    <FormGetter :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import FormGetter from './FormGetter.vue'
import Button from './Button.vue'
import Textbox from './Textbox.vue'

export default {
  components:{
    FormGetter,
    Button,
    Textbox,
  },
  data(){
    return{
      Mnum: "",
      Api: "http://167.99.6.44:8004/formsstudent/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeMnu(value)
    {
        this.Mnum = value
    },
    Click(){
      this.Send = this.Api + this.Mnum
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
