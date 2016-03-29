import React from 'react'
import { render } from 'react-dom'
import { ScatterChart } from 'react-d3'
import request from 'superagent'

export default class Chart extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      mailData: [{ values: [] }]
    }
  }

  componentDidMount() {
    request.get('./../../../data/mail_data_processed.json')
      .then(res => {
        this.setState({
          mailData: [{
            name: 'mailData',
            values: res.body.map(mail => ({ 
              x: new Date(mail.date_ms * 1000), 
              y: mail.subjectivity
            }))
          }]
        })
      })
  }

  render() {
    const { mailData } = this.state
    const isDataPopulated = !!mailData[0].values.length
    return (
      <div className="chart-container">
        <div className="filler"></div>
        { isDataPopulated && <ScatterChart
          data={mailData}
          width={800}
          height={800}
          title="Subjectivity of my emails over time"
          xAxisTickInterval={{unit: 'year', interval: 1}}
          xAxisLabel="Year"
          yAxisLabel="Subjectivity"
        /> }
      </div>
    )
  }
}