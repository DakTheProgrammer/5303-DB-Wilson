<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="Time Start" :maxLen="8" @getText = "ChangeSta"/>
    <br>
    <br>
    <Textbox message="Time End" :maxLen="8" @getText = "ChangeEnd"/>
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
      Start: "",
      End: "",
      Api: "http://167.99.6.44:8004/times/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeSta(value){
        this.Start = value
    },
    ChangeEnd(value){
        this.End = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Start + "/" + this.End + "/" + this.Semester
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
