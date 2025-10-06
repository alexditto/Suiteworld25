/**!
 * @file Team 5 SuiteLet Processor
 *
 * @note Absolutely zero security here
 *
 * @NScriptType Suitelet
 * @NApiVersion 2.1
 * @author Rob Vice
 * @version 0.0.1
 * @copyright 2025
 */

import { https, log, record, task } from 'N';
import { EntryPoints } from 'N/types';

export function onRequest(context: EntryPoints.Suitelet.onRequestContext): void {
  const simulatedCode: number = context.request.parameters.SimulatedCode;
  const _t5Record: record.Record = undefined;
  let simulatedResult = undefined;

  // Initialize endpoint data
  switch (context.request.parameters.EndpointKey) {
    case 'create':
      try {
        log.debug({
          title: 'Create ' + context.request.parameters.Title,
          details: context.request.body
        });

        this._t5Record = record.create({
          type:'customrecord_t5_model_record',
          isDynamic: true
        });

        this._t5Record.setText({
          fieldId: 'custrecord_t5_model_data',
          text: context.request.body
        });

        const recordId = this._t5Record.save();

        context.response.write(JSON.stringify({
            modelRecord: recordId
          }
        ));
      } catch (e) {
        log.debug({
          title: 'Unhandled netsuiteLogOnly Error',
          details: e
        });

          context.response.write(JSON.stringify({
            Error: e
          }
        ));
      }
      return;

    default:
      log.error({
        title: 'Error',
        details: 'Unrecognized endpoint: '.concat(context.request.parameters.EndpointKey)
      });

      context.response.write(JSON.stringify({
        error: 'Unrecognized endpoint '.concat(context.request.parameters.EndpointKey)
      }));
      return;
  }
}
