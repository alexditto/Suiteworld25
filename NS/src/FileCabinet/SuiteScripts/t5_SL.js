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
define(["require", "exports", "N"], function (require, exports, N_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.onRequest = onRequest;
    function onRequest(context) {
        const simulatedCode = context.request.parameters.SimulatedCode;
        const _t5Record = undefined;
        let simulatedResult = undefined;
        // Initialize endpoint data
        switch (context.request.parameters.EndpointKey) {
            case 'create':
                try {
                    N_1.log.debug({
                        title: 'Create ' + context.request.parameters.Title,
                        details: context.request.body
                    });
                    this._t5Record = N_1.record.create({
                        type: 'customrecord_t5_model_record',
                        isDynamic: true
                    });
                    this._t5Record.setText({
                        fieldId: 'custrecord_t5_model_data',
                        text: context.request.body
                    });
                    const recordId = this._t5Record.save();
                    context.response.write(JSON.stringify({
                        modelRecord: recordId
                    }));
                }
                catch (e) {
                    N_1.log.debug({
                        title: 'Unhandled netsuiteLogOnly Error',
                        details: e
                    });
                    context.response.write(JSON.stringify({
                        Error: e
                    }));
                }
                return;
            default:
                N_1.log.error({
                    title: 'Error',
                    details: 'Unrecognized endpoint: '.concat(context.request.parameters.EndpointKey)
                });
                context.response.write(JSON.stringify({
                    error: 'Unrecognized endpoint '.concat(context.request.parameters.EndpointKey)
                }));
                return;
        }
    }
});
