<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Button @pressed= "Click"/>
    <SimpleFormGetter :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import Button from './Button.vue'
import Dropdown from './Dropdown.vue'
import SimpleFormGetter from './SimpleFormGetter.vue'


export default {
  components:{
    Dropdown,
    Button,
    SimpleFormGetter
  },
  data(){
    return{
      Semester: "spring 2022",
      Gpa: "",
      Api: "http://167.99.6.44:8004/formssemster/",
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
