<template>
  <span id='pop'>
        <label for='Type'>Type:</label>
        <select name='Type' v-model="selected" @change="SendPorP()">
            <option value="New">New</option>
            <option value="Update">Update</option>
            <option value="a" hidden disabled>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</option>
        </select>
  </span>
</template>

<script>

export default {
  data(){
    return{
      selected: "New"
    }
  },
  methods:{
    SendPorP(){
      this.$emit('getPutOrPush', this.selected)
    }
  }
}
</script>

<style>
#pop
{
  position: relative;
  right: 55px;
}
</style>
