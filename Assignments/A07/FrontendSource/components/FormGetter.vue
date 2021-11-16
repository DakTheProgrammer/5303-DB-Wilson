<template>
    <div>
        <br>
        {{error}}
        <template v-for="i in titles.length" :key="i.whyisthisevenathingifitisusless">
            <h2>{{titles[i - 1]}}</h2>
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
                <template v-for="l in result[i - 1][1].length" :key="l.something">
                    <div id='len'>
                        <p id='row' class="a" v-if="l % 5 == 1">{{result[i - 1][1][l - 1]}}</p>
                        <p id='row' class="b" v-if="l % 5 == 2">{{result[i - 1][1][l - 1]}}</p>
                        <p id='row' class="c" v-if="l % 5 == 3">{{result[i - 1][1][l - 1]}}</p>
                        <p id='row' class="d" v-if="l % 5 == 4">{{result[i - 1][1][l - 1]}}</p>
                        <p id='row' class="e" v-if="l % 5 == 0">{{result[i - 1][1][l - 1]}}</p>
                    </div>
                    <br v-if="l % columns.length == 0 && l != 0">
                </template>
            </div>

        </template>
    </div>
</template>

<script>

export default {
  components:{

  },
  data(){
    return{
        titles: [],
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
            const response = await fetch(this.apiurl);
            const data = await response.json();
            this.titles = Object.keys(data.result)
            this.result = []
            var temp = []

            for(var i = 0; i < this.titles.length; i++)
            {
                if(this.columns.length == 0 && data.result[this.titles[i]].length != 0)
                {
                    this.columns = Object.keys(data.result[this.titles[0]][0])
                    i = 300
                }
            }

            for(i = 0; i < this.titles.length; i++)
            {
                temp = []
                for(var j = 0; j < data.result[this.titles[i]].length; j++)
                {
                    for(var l = 0; l < this.columns.length; l++)
                    {
                        temp.push(data.result[this.titles[i]][j][this.columns[l]])
                    }
                }
            
                if(data.result[this.titles[i]].length == 0)
                {
                    this.result.push([i, []])
                }
                else
                {
                    this.result.push([i, temp])
                }
            }
            this.show = true
            this.error = ""
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
