<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="Subject" :maxLen="4" @getText = "ChangeSub"/>
    <Button @pressed= "Click"/>
    <Geters :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import Button from './Button.vue'
import Dropdown from './Dropdown.vue'
import Geters from './Geters.vue'
import Textbox from './Textbox.vue'


export default {
  components:{
    Dropdown,
    Textbox,
    Button,
    Geters
  },
  data(){
    return{
      Semester: "spring 2022",
      Subject: "",
      Api: "http://167.99.6.44:8004/coursesubject/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeSub(value){
        this.Subject = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Subject + "/" + this.Semester
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
