<template>
    <div>
        <br>
        {{error}}
            <template v-for="j in columns" :key="j.lol">
                <div id='len'>
                    <p id='col' class="a" v-if="j == `M#`">{{j}}</p>
                    <p id='col' class="b" v-if="j == `First`">{{j}}</p>
                    <p id='col' class="c" v-if="j == `Last`">{{j}}</p>
                    <p id='col' class="d" v-if="j == `Courses`">{{j}}</p>
                    <p id='col' class="e" v-if="j == `Date`">{{j}}</p>
                </div>
            </template>
            <br>

            <div v-if="show">
                <template v-for="l in result.length" :key="l.something">
                    <div id='len'>
                        <p id='row' class="a" v-if="l % 5 == 1">{{result[l - 1]}}</p>
                        <p id='row' class="b" v-if="l % 5 == 2">{{result[l - 1]}}</p>
                        <p id='row' class="c" v-if="l % 5 == 3">{{result[l - 1]}}</p>
                        <p id='row' class="d" v-if="l % 5 == 4">{{result[l - 1]}}</p>
                        <p id='row' class="e" v-if="l % 5 == 0">{{result[l - 1]}}</p>
                    </div>
                    <br v-if="l % columns.length == 0 && l != 0">
                </template>
            </div>
    </div>
</template>

<script>

export default {
  components:{

  },
  data(){
    return{
        columns: [],
        result: [],
        rows: 0,
        show: false,
        error: "",
    }
  },
  props:{
    apiurl: String,
    test: Number
  },
  watch:{
    test: function()
    {
      this.ApiCall()
    }
  },
  methods:{
    async ApiCall()
    {
        try
        {
            this.error = ""
            this.show = false
            this.result = []
            const response = await fetch(this.apiurl);
            const data = await response.json();//data.result is an array
            this.columns = Object.keys(data.result[0])
            this.rows = data.result.length

            for(var i = 0; i < data.result.length; i++)
            {
            for(var j = 0; j < this.columns.length; j++)
            {
                this.result.push(data.result[i][this.columns[j]])
            }
            }
            this.show = true

            //console.log(data.result)
        }
        catch
        {
            this.error = "DOES NOT EXIST"
        }
    }
  },
  
}
</script>

<style>
#col
{
   display: inline;
   border-bottom: 1px solid;
}

#row
{
    display : inline;
    border-bottom:double;
}

#len
{
    display: inline-flex;
    text-align: left;
}

.a
{

    width: 130px;
}

.b
{

    width: 150px;
}

.c
{

    width: 150px;
}

.d
{

    width: 340px;
}

.e
{

    width: 80px;
}

</style>
