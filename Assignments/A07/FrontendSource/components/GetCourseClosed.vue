<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Button @pressed= "Click"/>
    <Geters :apiurl="Send" :test="Show"/>
  </div>
</template>

<script>
import Button from './Button.vue'
import Dropdown from './Dropdown.vue'
import Geters from './Geters.vue'

export default {
  components:{
    Dropdown,
    Button,
    Geters
  },
  data(){
    return{
      Semester: "spring 2022",
      Api: "http://167.99.6.44:8004/closed/",
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
