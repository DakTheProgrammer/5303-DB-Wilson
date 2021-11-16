<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="Crn" :maxLen="5" @getText = "ChangeCrn"/>
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
      Crn: "",
      Api: "http://167.99.6.44:8004/courseid/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeCrn(value){
        this.Crn = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Crn + "/" + this.Semester
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
