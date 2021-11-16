<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="Buidling" :maxLen="4" @getText = "ChangeBui"/>
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
      Building: "",
      Api: "http://167.99.6.44:8004/coursebuilding/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeBui(value){
        this.Building = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Building + "/" + this.Semester
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
