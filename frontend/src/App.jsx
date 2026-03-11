import { useState } from "react"
import axios from "axios"

function App() {

  const [file,setFile] = useState(null)
  const [email,setEmail] = useState("")
  const [result,setResult] = useState("")

  const submit = async () => {

    const formData = new FormData()
    formData.append("file",file)
    formData.append("email",email)

    const res = await axios.post("http://127.0.0.1:8000/analyze",formData)

    setResult(res.data.summary)
  }

  return (
    <div style={{padding:"40px"}}>

      <h2>Sales Insight Automator</h2>

      <input type="file" onChange={(e)=>setFile(e.target.files[0])}/>
      <br/><br/>

      <input
        placeholder="Enter email"
        onChange={(e)=>setEmail(e.target.value)}
      />

      <br/><br/>

      <button onClick={submit}>Generate Insight</button>

      <pre>{result}</pre>

    </div>
  )
}

export default App