<template>
  <div>
    <Dropdown @getDropdown= "ChangeSem"/>
    <Textbox message="Professor" :maxLen="100" @getText = "ChangePro"/>
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
      prof: "",
      Api: "http://167.99.6.44:8004/courseprofname/",
      Send: "",
      Show: 0,
    }
  },
  methods:{
    ChangePro(value){
        this.prof = value
    },
    ChangeSem(value){
      this.Semester = value
    },
    Click(){
      this.Send = this.Api + this.prof + "/" + this.Semester
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
