// nexlify_estimation - Project Estimation Client Script (Clean & Frappe 16 Safe)
// File: apps/nexlify_estimation/nexlify_estimation/public/js/estimation_controller.js

frappe.ui.form.on('Project Estimation', {
    refresh: function(frm) {
        load_opportunity_rfq(frm);
    },

    nexlify_estimation_opportunity: function(frm) {
        load_opportunity_rfq(frm);
    }
});


// ======================================
// Load RFQ from Opportunity
// ======================================
function load_opportunity_rfq(frm) {
    const opp = frm.doc.nexlify_estimation_opportunity;
    const html_field = 'nexlify_estimation_opportunity_rfq_html';

    if (!opp) {
        frm.set_df_property(html_field, 'options', '');
        apply_rfq_options(frm, []);
        return;
    }

    frappe.db.get_doc('Opportunity', opp).then(doc => {
        let items = doc.nexlify_rfq_table || [];

        // Build HTML
        let html = build_rfq_table(items);
        frm.set_df_property(html_field, 'options', html);

        // Extract unique items
        let options = [...new Set(
            items
                .map(i => i.nexlify_estimation_opportunity_rfq_item)
                .filter(Boolean)
        )];

        apply_rfq_options(frm, options);
    });
}


// ======================================
// Apply Select Options (Frappe 16 Safe)
// ======================================
function apply_rfq_options(frm, options_array) {
    let options_str = ['']
        .concat(options_array)
        .join('\n');

    let grid_field = frm.get_field('nexlify_estimation_tasks_table');

    if (!grid_field || !grid_field.grid) {
        return;
    }

    grid_field.grid.update_docfield_property(
        'nexlify_estimation_rfq_item',
        'options',
        options_str
    );

    grid_field.grid.refresh();
}


// ======================================
// RFQ HTML Table
// ======================================
function build_rfq_table(items) {
    if (!items || !items.length) {
        return `
            <div style="padding:15px;margin-top:10px;border:1px solid var(--border-color);border-radius:var(--border-radius);background:var(--control-bg);color:var(--text-color);">
                No RFQ items recorded for this opportunity.
            </div>
        `;
    }

    let rows = items.map(item => {
        return `
            <tr>
                <td>${item.nexlify_estimation_opportunity_rfq_item || ''}</td>
                <td>${item.nexlify_estimation_opportunity_rfq_description || ''}</td>
                <td>${item.nexlify_estimation_opportunity_rfq_uom || '-'}</td>
                <td style="font-weight:600;">${item.nexlify_estimation_opportunity_rfq_quantity || 0}</td>
            </tr>
        `;
    }).join('');

    return `
        <div class="table-responsive" style="margin-top:10px;border:1px solid var(--border-color);border-radius:var(--border-radius);background:var(--bg-color);">
            <table class="table table-bordered table-hover" style="margin-bottom:0;color:var(--text-color);">
                <thead style="background-color:var(--control-bg);">
                    <tr>
                        <th>Item</th>
                        <th>Description</th>
                        <th>UOM</th>
                        <th>Qty</th>
                    </tr>
                </thead>
                <tbody>
                    ${rows}
                </tbody>
            </table>
        </div>
    `;
}