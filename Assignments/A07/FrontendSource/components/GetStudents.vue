<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Button @pressed= "Click"/>
    <GetterStudent :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import Button from './Button.vue'
import Dropdown from './Dropdown.vue'
import GetterStudent from './GetterStudent.vue'


export default {
  components:{
    Dropdown,
    Button,
    GetterStudent,
  },
  data(){
    return{
      Semester: "spring 2022",
      Crn: "",
      Api: "http://167.99.6.44:8004/students/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.Semester
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
