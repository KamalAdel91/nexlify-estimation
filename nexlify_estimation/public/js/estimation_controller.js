// nexlify_estimation - Project Estimation Client Script
// File: apps/nexlify_estimation/nexlify_estimation/public/js/estimation_controller.js

frappe.ui.form.on('Project Estimation', {
    refresh: function(frm) {
        load_opportunity_rfq(frm);
    },
    nexlify_estimation_opportunity: function(frm) {
        load_opportunity_rfq(frm);
    }
});

function load_opportunity_rfq(frm) {
    const opp = frm.doc.nexlify_estimation_opportunity;
    const html_field = 'nexlify_estimation_opportunity_rfq_html';
    
    if (!opp) {
        frm.set_df_property(html_field, 'options', '');
        update_grid_options(frm, []);
        return;
    }

    frappe.db.get_doc('Opportunity', opp).then(doc => {
        let items = doc.nexlify_rfq_table || []; 
        
        // 1. تحديث وعرض جدول الـ HTML المعرب والمتوافق مع الثيمات
        let html = build_rfq_table(items);
        frm.set_df_property(html_field, 'options', html);

        // 2. استخراج الأصناف الفريدة لتحديث القائمة المنسدلة في الجدول الفرعي
        let options = items.map(i => i.nexlify_estimation_opportunity_rfq_item).filter(Boolean);
        options = [...new Set(options)];
        
        update_grid_options(frm, options);
    });
}

function update_grid_options(frm, options_array) {
    // بناء نص الخيارات مفصولة بسطر جديد كما يتطلب حقل Select في الفريم ورك
    let options_str = [''].concat(options_array).join('\n');
    
    // الوصول الصحيح لخصائص الحقل داخل الجدول الفرعي
    let docfield = frappe.meta.get_docfield('Project Estimation Tasks', 'nexlify_estimation_rfq_item');
    if (docfield) {
        docfield.options = options_str;
    }
    
    // إجبار الجدول الفرعي (Grid) على إعادة بناء نفسه لقراءة الخيارات المحقونة حديثاً
    if (frm.fields_dict['nexlify_estimation_tasks_table'] && frm.fields_dict['nexlify_estimation_tasks_table'].grid) {
        frm.fields_dict['nexlify_estimation_tasks_table'].grid.refresh();
    }
}

function build_rfq_table(items) {
    if (!items || !items.length) {
        return `
            <div style="padding: 15px; margin-top: 10px; border: 1px solid var(--border-color); border-radius: var(--border-radius); background-color: var(--control-bg); color: var(--text-color);">
                No RFQ items recorded for this opportunity.
            </div>
        `;
    }

    let rows = items.map(item => {
        return `
            <tr>
                <td style="vertical-align: middle;">${item.nexlify_estimation_opportunity_rfq_item || ''}</td>
                <td style="vertical-align: middle;">${item.nexlify_estimation_opportunity_rfq_description || ''}</td>
                <td style="vertical-align: middle;">${item.nexlify_estimation_opportunity_rfq_uom || '-'}</td>
                <td style="vertical-align: middle; font-weight: 600;">${item.nexlify_estimation_opportunity_rfq_quantity || 0}</td>
            </tr>
        `;
    }).join('');

    return `
        <div class="table-responsive" style="margin-top: 10px; border: 1px solid var(--border-color); border-radius: var(--border-radius); overflow-x: auto; background-color: var(--bg-color);">
            <table class="table table-bordered table-hover" style="margin-bottom: 0; color: var(--text-color);">
                <thead style="background-color: var(--control-bg);">
                    <tr>
                        <th style="font-weight: 600; border-bottom: 1px solid var(--border-color);">Item</th>
                        <th style="font-weight: 600; border-bottom: 1px solid var(--border-color);">Description</th>
                        <th style="font-weight: 600; border-bottom: 1px solid var(--border-color);">UOM</th>
                        <th style="font-weight: 600; border-bottom: 1px solid var(--border-color);">Qty</th>
                    </tr>
                </thead>
                <tbody>
                    ${rows}
                </tbody>
            </table>
        </div>
    `;
}