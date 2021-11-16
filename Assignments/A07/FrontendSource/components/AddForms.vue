<template>
  <div>
    <h1>{{ErrorMessage}}</h1>
    <PutOrPush @getPutOrPush = "ChangeSen"/>
    <Dropdown @getDropdown= "ChangeSem"/>
    <br>
    <br>
    <Textbox message= "M#" :maxLen="12" @getText = "ChangeMnu"/>
    <Textbox message= "First" :maxLen="35" @getText = "ChangeFir"/>
    <br>
    <br>
    <Textbox message= "Last" :maxLen="35" @getText = "ChangeLas"/>
    <Textbox message= "Courses" :maxLen="100" @getText = "ChangeCou"/>
    <br>
    <br>
    <Textbox message= "Date" :maxLen="10" @getText = "ChangeDat"/>
    <Button @pressed= "Click"/>
  </div>

</template>

<script>
import Dropdown from "./Dropdown.vue"
import Textbox from "./Textbox.vue"
import Button from "./Button.vue"
import PutOrPush from "./PutOrPush.vue"

export default {
  components:{
    Textbox,
    Dropdown,
    Button,
    PutOrPush
  },
  data(){
    return{
        ErrorMessage: "",
        Send: "New",
        Semester: "spring 2022",
        Mnum: "",
        First: "",
        Last: "",
        Courses: "",
        Date: "",
    }
  },
  methods:{
    async Click() {
      if(this.Send == "New")
      {
        try
        {
          const options = {method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({
          "Semester": this.Semester,
          "M#": this.Mnum,
          "First": this.First,
          "Last": this.Last,
          "Courses": this.Courses,
          "Date": this.Date})} 

          await fetch("http://167.99.6.44:8004/addform", options);
          //const response = await fetch("http://167.99.6.44:8004/addform", options);
          //const data = await response.json();
          this.ErrorMessage = "Success!"
        }
        catch
        {
          this.ErrorMessage = "Must give a unique M#"
        }
        
      }
      else if(this.Send == "Update")
      {
        const sender = {method: "GET"} 

        const get = await fetch("http://167.99.6.44:8004/formsstudentsemester/" + this.Mnum + "/" + this.Semester, sender);
        const stuff = await get.json();

        if(stuff.result.length != 0)
        {
          const options = {method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify({
          "Semester": this.Semester,
          "M#": this.Mnum,
          "First": this.First,
          "Last": this.Last,
          "Courses": this.Courses,
          "Date": this.Date})} 
          await fetch("http://167.99.6.44:8004/editform", options);
          //const response = await fetch("http://167.99.6.44:8004/editform", options);
          //const data = await response.json();
          this.ErrorMessage = "Success!"
        }
        else
        {
          this.ErrorMessage = "No M# in database by given M#"
        }
      }
      
    },
    ChangeMnu(value){
      this.Mnum = value
    },
    ChangeFir(value){
      this.First = value
    },
    ChangeLas(value){
      this.Last = value
    },
    ChangeCou(value){
      this.Courses = value
    },
    ChangeDat(value){
      this.Date = value
    },
    ChangeSem(value)
    {
      this.Semester = value
    },
    ChangeSen(value)
    {
      this.Send = value
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
