<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="Course Number" :maxLen="4" @getText = "ChangeCnu"/>
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
      Cnum: "",
      Api: "http://167.99.6.44:8004/coursenum/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeCnu(value){
        this.Cnum = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Cnum + "/" + this.Semester
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
