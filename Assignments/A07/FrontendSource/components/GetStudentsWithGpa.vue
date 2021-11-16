<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="GPA" :maxLen="5" @getText = "ChangeGpa"/>
    <Button @pressed= "Click"/>
    <GetterStudent :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import Button from './Button.vue'
import Dropdown from './Dropdown.vue'
import GetterStudent from './GetterStudent.vue'
import Textbox from './Textbox.vue'


export default {
  components:{
    Dropdown,
    Textbox,
    Button,
    GetterStudent,
  },
  data(){
    return{
      Semester: "spring 2022",
      Gpa: "",
      Api: "http://167.99.6.44:8004/studentsgpa/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeGpa(value){
        this.Gpa = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Semester + "/" + this.Gpa
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
